from rest_framework import viewsets

from gmao.pagination import CustomPageNumberPagination
from ..serializers import EquipmentFamilySerializer, EquipmentSerializer
from ..models import EquipmentModel, EquipmentFamilyModel
from django_filters.rest_framework import DjangoFilterBackend # to filter the queryset
from rest_framework import filters # to filter the queryset


class EquipmentViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = EquipmentModel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room_id','family_id','id']  # to filter by facility name or facility id
    ordering_fields = ['room_id','family_id','id']  # to order by facility name or facility id


class EquipmentFamilyViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentFamilySerializer
    queryset = EquipmentFamilyModel.objects.all()

# EquipmentPaginationViewSet is used to paginate the queryset
class EquipmentPaginationViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = EquipmentModel.objects.all().order_by('id') # to order the queryset for pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room_id','id','family_id','name','room_id__room']  # to filter by facility name or facility id
    ordering_fields = ['room_id','id','family_id','name','room_id__room']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to set the pagination class

#EquipmentFamilyPaginationViewset is used to paginate the queryset
class EquipmentFamilyPaginationViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentFamilySerializer
    queryset = EquipmentFamilyModel.objects.all().order_by('id') # to order the queryset for pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['id','parent_id','parent_id__name','name']  # to filter by facility name or facility id
    ordering_fields = ['id','parent_id','parent_id__name','name']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to set the pagination class