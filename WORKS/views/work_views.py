from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from ..models.work_models import WorkStatusModel, WorkOrderModel, WorkOrderStatusModel, WorkOrderPictureModel, \
    WorkOrderHourModel
from ..serializers.work_serializers import WorkStatusSerializer, WorkOrderSerializer, WorkOrderStatusSerializer, \
    WorkOrderPictureSerializer, WorkOrderHourSerializer
from django_filters.rest_framework import DjangoFilterBackend  # to filter the queryset
from rest_framework import filters  # to filter the queryset
from gmao.pagination import CustomPageNumberPagination  # to use our custom pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    ordering_fields = ['event_date_time','work_order','author','status_before','status_after','id']  # to order by event_date_time



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
    filterset_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id','job__job',
                        'room__floor__facility__facility_name','room__room','status__name','assignee__username']  # to filter by room
    ordering_fields = ['room', 'job_type', 'status', 'equipment', 'assignee', 'job', 'domain','id','job__job',
                       'room__floor__facility__facility_name','room__room','status__name','assignee__username']  # to order by room
    pagination_class = CustomPageNumberPagination  # to paginate the list

# WorkOrderHourPaginationViewset is used to paginate the work order list
class WorkOrderHourPaginationViewset(viewsets.ModelViewSet):
    queryset = WorkOrderHourModel.objects.all().order_by('id')
    serializer_class = WorkOrderHourSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['work_order','id','worker','start_datetime','end_datetime']  # to filter by work_order
    ordering_fields = ['work_order','id','worker','start_datetime','end_datetime']  # to order by work_order
    pagination_class = CustomPageNumberPagination  # to paginate the list

# WorkStatusPaginationViewset is used to paginate the work order list
class WorkStatusPaginationViewset(viewsets.ModelViewSet):
    queryset = WorkStatusModel.objects.all().order_by('id')
    serializer_class = WorkStatusSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    pagination_class = CustomPageNumberPagination  # to paginate the list
    filterset_fields = ['id','name','position']  # to filter by work_order
    ordering_fields = ['id','name','position']  # to order by work_order

#APIview DeletePreventiveWo is used to delete workorders having workorder_status in first position + job_type = preventive
class DeletePreventiveWo(APIView):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    #loop on all workorders having workorder_status in first position + job_type = preventive
    def post(self, request):
        #get position of workorder_status in position having lowest integer value
        first_position = WorkStatusModel.objects.order_by('position').first().position
        print("AZIZ first_position",first_position)
        is_deleted = False
        #loop on all workorders having workorder_status in first position + job_type = preventive
        for workorder in WorkOrderModel.objects.filter(job_type__name="préventif", status__position=first_position):
            #delete the workorder
            workorder.delete()
            is_deleted = True
        if is_deleted:
            content = {'DELETE PREVENTIVE WO': 'DELETION DONE'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'DELETE PREVENTIVE WO': 'NO DELETION DONE'}
            return Response(content, status=status.HTTP_304_NOT_MODIFIED)