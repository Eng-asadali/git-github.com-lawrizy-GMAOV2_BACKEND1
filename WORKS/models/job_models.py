from django.db import models

class JobTypeModel(models.Model):
    """
    Job Type est utilisé pour CORRECTIF - PREVENTIF - SEC
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name