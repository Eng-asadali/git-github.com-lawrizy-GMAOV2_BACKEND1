from rest_framework import viewsets
from ..serializers import EquipmentFamilySerializer, EquipmentSerializer
from ..models import EquipmentModel, EquipmentFamilyModel
from django_filters.rest_framework import DjangoFilterBackend # to filter the queryset
from rest_framework import filters # to filter the queryset


class EquipmentViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = EquipmentModel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room_id']  # to filter by facility name or facility id


class EquipmentFamilyViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentFamilySerializer
    queryset = EquipmentFamilyModel.objects.all()
