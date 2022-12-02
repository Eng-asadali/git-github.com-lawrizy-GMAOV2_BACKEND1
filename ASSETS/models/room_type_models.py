from django.db import models


class RoomTypeModel(models.Model):
    room_type = models.CharField(max_length=40, null=False, blank=False, unique=True)
    code = models.CharField(max_length=2, null=False, blank=False, unique=False)  # attention on le code n'est pas unique

    class Meta:
        indexes = [
            models.Index(fields=['room_type']),
        ]

    def __str__(self):
        value = (self.room_type+" -- "+self.code)
        return value
