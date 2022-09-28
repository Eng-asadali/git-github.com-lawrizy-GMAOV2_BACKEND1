from rest_framework import viewsets
from ..serializers import EquipmentFamilySerializer, EquipmentSerializer
from ..models import EquipmentModel, EquipmentFamilyModel


class EquipmentViewset(viewsets.ViewSet):
    serializer = EquipmentSerializer
    queryset = EquipmentModel.objects.all()


class EquipmentFamilyViewset(viewsets.ViewSet):
    serializer = EquipmentFamilySerializer
    queryset = EquipmentFamilyModel.objects.all()
