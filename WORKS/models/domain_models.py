from django.db import models


class DomainModel(models.Model):
    """
    domain est utilisé pour HVAC, SANITAIRE....
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name