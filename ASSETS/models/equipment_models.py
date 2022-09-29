from django.db import models
from.room_models import RoomModel


class EquipmentFamilyModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    parent_id = models.ForeignKey('self', on_delete=models.PROTECT, null=True, related_name='children', blank=True)

    def __str__(self):
        return self.name


class EquipmentModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    parent_id = models.ForeignKey('self', on_delete=models.PROTECT, null=True, related_name='children', blank=True)
    room_id = models.ForeignKey(RoomModel, on_delete=models.PROTECT, null=True, related_name='equipment')
    family_id = models.ForeignKey(EquipmentFamilyModel, on_delete=models.PROTECT, null=True, related_name='family_children')

    def __str__(self):
        return self.name


