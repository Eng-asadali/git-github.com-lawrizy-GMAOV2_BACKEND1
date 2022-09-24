from django.db import models
from .floor_models import FloorModel


class RoomModel(models.Model):
    room = models.CharField(max_length=100, null=False, blank=False)
    floor = models.ForeignKey(FloorModel, on_delete=models.PROTECT, null=False, related_name='room')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['room', 'floor'], name='uniqueConst_1_room_per_floor')]

    def __str__(self):
        return self.room
