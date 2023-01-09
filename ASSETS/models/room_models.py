from django.db import models
from .floor_models import FloorModel
from .facility_models import Facility
from .room_type_models import RoomTypeModel


class RoomModel(models.Model):
    room = models.CharField(max_length=100, null=False, blank=False, unique=True)
    floor = models.ForeignKey(FloorModel, on_delete=models.PROTECT, null=False, related_name='room')
    room_type = models.ForeignKey(RoomTypeModel, on_delete=models.PROTECT, null=False, related_name="room")


    class Meta:
        indexes = [
            models.Index(fields=['room', 'floor', 'room_type']),
        ]
        #  constraints = [models.UniqueConstraint(fields=['room', 'floor'], name='uniqueConst_1_room_per_floor')]

    def __str__(self):
        content = self.room + " -- " + self.room_type.room_type
        return content
