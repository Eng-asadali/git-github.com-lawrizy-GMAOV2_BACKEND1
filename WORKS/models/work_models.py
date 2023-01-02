from django.db import models
from ASSETS.models import RoomModel, EquipmentModel
from .job_models import JobTypeModel, JobModel, DomainModel
from django.contrib.auth.models import User


# WorkStatusModel contiendra les status: todo, in_progress,closed
class WorkStatusModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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
        return self.title


# WorkOrderStatus cette table fait le lien entre status et work
class WorkOrderStatusModel(models.Model):
    work_order = models.ForeignKey(WorkOrderModel, on_delete=models.CASCADE,related_name='work_order_status')
    event_date_time = models.DateTimeField(auto_now_add=True)
    status_before = models.ForeignKey(WorkStatusModel, on_delete=models.PROTECT,
                                      null=True, related_name='before_wo_status')
    status_after = models.ForeignKey(WorkStatusModel, on_delete=models.PROTECT,
                                     null=True, related_name='after_wo_status')
