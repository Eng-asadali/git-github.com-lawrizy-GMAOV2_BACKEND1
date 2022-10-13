from rest_framework import viewsets
from ..models.work_models import WorkStatusModel, WorkOrderModel, WorkOrderStatusModel
from ..serializers.work_serializers import WorkStatusSerializer, WorkOrderSerializer, WorkOrderStatusSerializer


class WorkStatusViewset(viewsets.ModelViewSet):
    queryset = WorkStatusModel.objects.all()
    serializer_class = WorkStatusSerializer


class WorkOrderViewset(viewsets.ModelViewSet):
    queryset = WorkOrderModel.objects.all()
    serializer_class = WorkOrderSerializer


class WorkOrderStatusViewset(viewsets.ModelViewSet):
    queryset = WorkOrderStatusModel.objects.all()
    serializer_class = WorkOrderStatusSerializer

