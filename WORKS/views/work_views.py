from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from ..models.work_models import WorkStatusModel, WorkOrderModel, WorkOrderStatusModel
from ..serializers.work_serializers import WorkStatusSerializer, WorkOrderSerializer, WorkOrderStatusSerializer
from ASSETS.models import RoomModel
from ASSETS.serializers import RoomSerializer
from rest_framework.response import Response


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
