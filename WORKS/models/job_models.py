from django.db import models
from .domain_models import DomainModel

class JobTypeModel(models.Model):
    """
    Job Type est utilisé pour le type d'intervention CORRECTIF - PREVENTIF - SEC
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class JobModel(models.Model):
    """
    Job est pour l'intervention, exemple: entretien mensuel
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    job_type_id = models.ForeignKey(JobTypeModel, on_delete=models.PROTECT, null=False, related_name='job_type')
    domain_id = models.ForeignKey(DomainModel, on_delete=models.PROTECT, null=False, related_name='domain')

    def __str__(self):
        return self.name
