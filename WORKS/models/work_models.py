from django.core.files import File
from django.core.files.storage import default_storage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ASSETS.models import RoomModel, EquipmentModel
from .job_models import JobTypeModel, JobModel, DomainModel
from django.contrib.auth.models import User
from PIL import Image  # used for image resizing
from .work_archive_models import WorkOrderArchiveModel, WorkOrderStatusArchiveModel
import uuid

from django.utils import timezone

# WorkStatusModel contiendra les status: todo, in_progress,closed
class WorkStatusModel(models.Model):
    name = models.CharField(max_length=255)
    position = models.IntegerField(blank=False, null=False, unique=False)

    def __str__(self):
        return self.name

    # add indexes for all the fields
    class Meta:
        indexes = [
            models.Index(fields=['name', 'position']),
        ]


# Work order model: contient les tickets
class WorkOrderModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    room = models.ForeignKey(RoomModel, on_delete=models.PROTECT, null=False, blank=False, related_name='work_order')
    job_type = models.ForeignKey(JobTypeModel, on_delete=models.PROTECT, null=False, blank=False, related_name='work_orders')
    status = models.ForeignKey(WorkStatusModel, on_delete=models.PROTECT, null=False)
    equipment = models.ForeignKey(EquipmentModel, on_delete=models.PROTECT, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name='reporter_wo')
    assignee = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='assignee_wo')
    job = models.ForeignKey(JobModel, on_delete=models.PROTECT, null=False, blank=False, related_name='work_orders')
    domain = models.ForeignKey(DomainModel, on_delete=models.PROTECT, null=False, blank=False, related_name='work_orders')
    creation_date = models.DateTimeField(auto_now_add=True) # auto_now_add is used when we create the first time the object
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # convert id to string

        return str(self.id)

    #make indexes for all the fields
    class Meta:
        indexes = [
            models.Index(fields=['title', 'description', 'room', 'job_type', 'status', 'equipment', 'reporter',
                                 'assignee', 'job', 'domain', 'creation_date', 'start_date', 'end_date'],
                         name='work_order_idx'),
        ]


# WorkOrderStatus cette table fait le lien entre status et work. Elle est utilisé pour garder l'historique des status et les commentaires
class WorkOrderStatusModel(models.Model):
    work_order = models.ForeignKey(WorkOrderModel, on_delete=models.CASCADE,related_name='work_order_status')
    event_date_time = models.DateTimeField(auto_now_add=True)
    status_before = models.ForeignKey(WorkStatusModel, on_delete=models.PROTECT,
                                      null=True, related_name='before_wo_status')
    status_after = models.ForeignKey(WorkStatusModel, on_delete=models.PROTECT,
                                     null=True, related_name='after_wo_status')
    comment = models.CharField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name='author_wo_status')

    # make indexes for all the fields
    class Meta:
        indexes = [
            models.Index(fields=['work_order', 'event_date_time', 'status_before', 'status_after']),
        ]

    def __str__(self):
        result = f"{self.work_order} -- {self.event_date_time} -- {self.status_before} -- {self.status_after}"
        return result


# work_order_picture_path is used to generate the path and the name of the picture file (wo_xx.jpg) --
# it is used in the WorkOrderPictureModel.picture field
def work_order_picture_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/work_order_pictures/work_order_<id>.jpg
    # add at the end a uuid to make sure the file name is unique (pour eviter que le cache du browser ne garde l'ancienne image)
    unique_id = uuid.uuid4().hex
    relative_name = 'work_order_pictures/wo_{0}_{1}.jpg'.format(instance.work_order.id,unique_id)
    return relative_name


class WorkOrderPictureModel(models.Model):
    work_order = models.ForeignKey(WorkOrderModel, on_delete=models.CASCADE, related_name='work_order_pictures')
    picture = models.ImageField(upload_to=work_order_picture_path, null=True, blank=True)  # upload_to uses the helper above

    # make indexes for all the fields
    class Meta:
        indexes = [
            models.Index(fields=['work_order', 'picture']),
        ]

    def __str__(self):
        result = f"{self.work_order} -- {self.picture}"
        return result

    # the save method is overriden to resize the image before saving it and to delete the old image
    # -- to limit to 1 image per work order
    def save(self, *args, **kwargs):
        print("AZIZ start save picture")
        try:
            old_picture = WorkOrderPictureModel.objects.get(work_order=self.work_order)
            # Delete the old image file
            default_storage.delete(old_picture.picture.path)
            old_picture.delete()
        except WorkOrderPictureModel.DoesNotExist:
            pass
        # Open image
        img = Image.open(self.picture)

        # Resize image
        MAX_SIZE = (640, 640)
        img.thumbnail(MAX_SIZE)

        # Save image
        MAX_SIZE_BYTES = 1 * 1024 * 1024  #  1 MB
        quality = 100
        if self.picture.size > MAX_SIZE_BYTES:
            while self.picture.size > MAX_SIZE_BYTES:
                quality -= 5
                img.save(self.picture.path, format='JPEG', quality=quality)
                # Update picture attribute with new image data
                with open(self.picture.path, 'rb') as f:
                    new_picture = File(f)
                    self.picture = new_picture

                print(f"AZIZ picture reduce: quality: {quality} -- size: {self.picture.size}")
                if quality <= 0:
                    raise ValueError("Cannot reduce file size.")
            with default_storage.open(self.picture.path, 'rb') as f: # open the file because it was
                # closed in the while loop and the super.save() will fail
                new_picture = File(f)
                self.picture = new_picture
                super(WorkOrderPictureModel, self).save(*args, **kwargs)
                print(f"AZIZ picture saved with quality change")
        else:
            super(WorkOrderPictureModel, self).save(*args, **kwargs)
            print(f"AZIZ picture saved")

# the archive_work_order function is called when a work order is archived in the work_serializer when the status is changed
# to 100 or more and the instance is saved
@receiver(post_save, sender=WorkOrderModel)
def archive_work_order(sender, instance, **kwargs):
    if instance.status.position >= 100:
        # Archive the work order by creating a new record in the WorkOrderArchiveModel
        WorkOrderArchiveModel.objects.create(
            room=instance.room,
            equipment=instance.equipment,
            domain=instance.domain,
            creation_date=instance.creation_date,
            description=instance.description,
            status=instance.status,
            reporter=instance.reporter,
            job=instance.job,
            job_type=instance.job_type,
            id=instance.id,
            assignee=instance.assignee,
            start_date=instance.start_date,
            end_date=timezone.now(),
        )
        # archive the work order status by creating a new record in the WorkOrderStatusArchiveModel
        for status in instance.work_order_status.all():
            WorkOrderStatusArchiveModel.objects.create(
                work_order=status.work_order.id,
                event_date_time=status.event_date_time,
                status_before=status.status_before,
                status_after=status.status_after,
                comment=status.comment,
                author=status.author,
            )
            # delete the work order status that was archived
            status.delete()

        # Delete the work order that was archived
        instance.delete()

#WorkHourModel is used to store the hours worked (startHour, endHour) on a work order by a user
class WorkOrderHourModel(models.Model):
    work_order = models.ForeignKey(WorkOrderModel, on_delete=models.CASCADE, related_name='work_hours')
    worker = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name='user_work_hours')
    start_datetime = models.DateTimeField(null=False, blank=False)
    end_datetime = models.DateTimeField(null=True, blank=True) # end_hour can be null if the user is still working on the work order
    comment = models.CharField(max_length=1000, null=True, blank=True)

    # make indexes for all the fields
    class Meta:
        indexes = [
            models.Index(fields=['work_order', 'worker', 'start_datetime', 'end_datetime']),
        ]

    def __str__(self):
        result = f"{self.work_order} -- {self.user} -- {self.start_hour} -- {self.end_hour}"
        return result