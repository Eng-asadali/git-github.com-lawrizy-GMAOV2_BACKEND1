from rest_framework import viewsets
from ..serializers import RoomTypeSerializer
from ..models import RoomTypeModel


class RoomTypeViewset(viewsets.ModelViewSet):
    queryset = RoomTypeModel.objects.all()
    serializer_class = RoomTypeSerializer
