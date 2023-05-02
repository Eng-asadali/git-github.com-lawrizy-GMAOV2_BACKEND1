from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from ..models.work_models import WorkStatusModel, WorkOrderModel, WorkOrderStatusModel, WorkOrderPictureModel
from ..serializers.work_serializers import WorkStatusSerializer, WorkOrderSerializer, WorkOrderStatusSerializer, \
    WorkOrderPictureSerializer
from django_filters.rest_framework import DjangoFilterBackend  # to filter the queryset
from rest_framework import filters  # to filter the queryset
from gmao.pagination import CustomPageNumberPagination  # to use our custom pagination


class WorkStatusViewset(viewsets.ModelViewSet):
    queryset = WorkStatusModel.objects.all()
    serializer_class = WorkStatusSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication


class WorkOrderViewset(viewsets.ModelViewSet):
    queryset = WorkOrderModel.objects.all()
    serializer_class = WorkOrderSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id']  # to filter by room
    ordering_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id']  # to order by room

class WorkOrderStatusViewset(viewsets.ModelViewSet):
    queryset = WorkOrderStatusModel.objects.all()
    serializer_class = WorkOrderStatusSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['work_order']  # to filter by work_order
    ordering_fields = ['event_date_time']  # to order by event_date_time



# I need a view that will be used to upload an image


class WorkOrderPictureViewset(viewsets.ModelViewSet):
    queryset = WorkOrderPictureModel.objects.all()
    serializer_class = WorkOrderPictureSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)  # to upload a file
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['work_order']  # to filter by work_order


# WorkOrderPaginationViewset is used to paginate the work order list
class WorkOrderPaginationViewset(viewsets.ModelViewSet):
    queryset = WorkOrderModel.objects.all().order_by('id')
    serializer_class = WorkOrderSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id']  # to filter by room
    ordering_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id']  # to order by room
    pagination_class = CustomPageNumberPagination  # to paginate the list
