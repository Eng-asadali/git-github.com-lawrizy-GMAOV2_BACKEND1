from rest_framework import viewsets
from ..serializers import RoomSerializer
from ..models import RoomModel


class RoomViewset(viewsets.ModelViewSet):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer
