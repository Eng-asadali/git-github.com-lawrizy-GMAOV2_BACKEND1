from django.db import models
from ASSETS.models import RoomModel, EquipmentModel
from .job_models import JobTypeModel, JobModel, DomainModel
from django.contrib.auth.models import User


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


# WorkOrderStatus cette table fait le lien entre status et work
class WorkOrderStatusModel(models.Model):
    work_order = models.ForeignKey(WorkOrderModel, on_delete=models.CASCADE,related_name='work_order_status')
    event_date_time = models.DateTimeField(auto_now_add=True)
    status_before = models.ForeignKey(WorkStatusModel, on_delete=models.PROTECT,
                                      null=True, related_name='before_wo_status')
    status_after = models.ForeignKey(WorkStatusModel, on_delete=models.PROTECT,
                                     null=True, related_name='after_wo_status')

    # make indexes for all the fields
    class Meta:
        indexes = [
            models.Index(fields=['work_order', 'event_date_time', 'status_before', 'status_after']),
        ]

    def __str__(self):
        result = f"{self.work_order} -- {self.event_date_time} -- {self.status_before} -- {self.status_after}"
        return result


class WorkOrderPictureModel(models.Model):
    work_order = models.ForeignKey(WorkOrderModel, on_delete=models.CASCADE, related_name='work_order_pictures')
    picture = models.ImageField(upload_to='work_order_pictures', null=True, blank=True)

    # make indexes for all the fields
    class Meta:
        indexes = [
            models.Index(fields=['work_order', 'picture']),
        ]

    def __str__(self):
        result = f"{self.work_order} -- {self.picture}"
        return result