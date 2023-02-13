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


class WorkOrderStatusViewset(viewsets.ModelViewSet):
    queryset = WorkOrderStatusModel.objects.all()
    serializer_class = WorkOrderStatusSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['work_order']  # to filter by work_order
    ordering_fields = ['event_date_time']  # to order by event_date_time

# this view will be used to get all the data from the 3 models
# to have 
# @api_view(['GET'])
# def wo_and_status_and_rooms(request):
#     if request.method == 'GET':
#         # first we get the querysets
#         wo = WorkOrderModel.objects.all()
#         rooms = RoomModel.objects.all()
#         # then we serializer the data
#         room_serializer = RoomSerializer(rooms, many=True, context={'request': request})
#         wo_serializer = WorkOrderSerializer(wo, many=True, context={'request': request})
#         data = room_serializer.data + wo_serializer.data
#         data = {"wo": wo_serializer.data, "rooms": room_serializer.data}
#         return Response(data)

# I need a view that will be used to upload an image


class WorkOrderPictureViewset(viewsets.ModelViewSet):
    queryset = WorkOrderPictureModel.objects.all()
    serializer_class = WorkOrderPictureSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)  # to upload a file
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['work_order']  # to filter by work_order
