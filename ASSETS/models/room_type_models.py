from django.db import models


class RoomTypeModel(models.Model):
    room_type = models.CharField(max_length=40, null=False, blank=False)
    code = models.CharField(max_length=2, null=False, blank=False)

    def __str__(self):
        value = (self.room_type+" -- "+self.code)
        return value
