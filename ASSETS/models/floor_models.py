from django.db import models
from .facility_models import Facility


class FloorModel(models.Model):
    floor = models.CharField(max_length=30, null=False, blank=False)
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT, null=False, related_name='floor')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['floor', 'facility'], name='unique_floor_per_facility'),
        ]
        