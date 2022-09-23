from rest_framework import viewsets
from ..serializers import FloorSerializer
from ..models import FloorModel


class FloorViewSet(viewsets.ModelViewSet):
    queryset = FloorModel.objects.all()
    serializer_class = FloorSerializer
