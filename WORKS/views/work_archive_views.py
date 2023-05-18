from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models.work_archive_models import WorkOrderArchiveModel, WorkOrderStatusArchiveModel
from ..serializers.work_archive_serializers import WorkOrderArchiveSerializer, WorkOrderStatusArchiveSerializer
from django_filters.rest_framework import DjangoFilterBackend  # to filter the queryset
from rest_framework import filters  # to filter the queryset
from gmao.pagination import CustomPageNumberPagination  # to use our custom pagination

class WorkOrderArchivePaginationViewset(viewsets.ModelViewSet):
    queryset = WorkOrderArchiveModel.objects.all().order_by('id')
    serializer_class = WorkOrderArchiveSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id']  # to filter by room
    ordering_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id']  # to order by room
    pagination_class = CustomPageNumberPagination  # to use our custom pagination



class WorkOrderStatusArchivePaginationViewset(viewsets.ModelViewSet):
    queryset = WorkOrderStatusArchiveModel.objects.all().order_by('id')
    serializer_class = WorkOrderStatusArchiveSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['event_date_time','work_order','author','status_before','status_after','id']  # to filter by work_order
    ordering_fields = ['event_date_time','work_order','author','status_before','status_after','id']  # to order by event_date_time
    pagination_class = CustomPageNumberPagination  # to use our custom pagination
