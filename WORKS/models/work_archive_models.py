from django.core.files import File
from django.core.files.storage import default_storage
from django.db import models
from ASSETS.models import RoomModel, EquipmentModel
from .job_models import JobTypeModel, JobModel, DomainModel
#from .work_models import WorkStatusModel
from django.contrib.auth.models import User

# Work order archive model: will store the closed work orders (having status position >=100) in read only mode and text only
# all the foreign keys will be replaced by the name of the object
class WorkOrderArchiveModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    room = models.CharField(max_length=255, null=False, blank=False)
    job_type = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=255, null=False, blank=False)
    equipment = models.CharField(max_length=255, null=True, blank=True)
    reporter = models.CharField(max_length=255, null=False, blank=False)
    assignee = models.CharField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=False, blank=False)
    domain = models.CharField(max_length=255, null=False, blank=False)
    creation_date = models.DateTimeField(null=True, blank=True)
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
                         name='work_order_archive_idx'),
        ]