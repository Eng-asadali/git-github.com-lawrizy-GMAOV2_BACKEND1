from rest_framework import viewsets
from ..serializers import EquipmentFamilySerializer, EquipmentSerializer
from ..models import EquipmentModel, EquipmentFamilyModel


class EquipmentViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = EquipmentModel.objects.all()


class EquipmentFamilyViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentFamilySerializer
    queryset = EquipmentFamilyModel.objects.all()
