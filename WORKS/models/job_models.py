from django.db import models

from ASSETS.models import EquipmentModel # used for the JobEquipmentModel
from .domain_models import DomainModel

class JobTypeModel(models.Model):
    """
    Job Type est utilisé pour le type d'intervention CORRECTIF - PREVENTIF - SEC
    """
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class JobModel(models.Model):
    """
    Job est pour l'intervention, exemple: entretien mensuel
    """
    job = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(blank=True,null=True)
    job_type_id = models.ForeignKey(JobTypeModel, on_delete=models.PROTECT, null=False, related_name='jobs')
    domain_id = models.ForeignKey(DomainModel, on_delete=models.PROTECT, null=False, related_name='jobs')
    frequency = models.IntegerField(null=True, blank=True) # frequency in days

    def __str__(self):
        return self.job

#JobEquipmentModel used to store the couple job/equipment for the preventive jobs that will trigger automatically work orders
class JobEquipmentModel(models.Model):
    job_id = models.ForeignKey(JobModel, on_delete=models.PROTECT, null=False, related_name='jobs')
    equipment_id = models.ForeignKey(EquipmentModel, on_delete=models.PROTECT, null=False, related_name='equipments')

    def __str__(self):
        return self.job_id.job + ' - ' + self.equipment_id.name

    #unicity constraint on the couple job/equipment
    class Meta:
        unique_together = ('job_id', 'equipment_id')