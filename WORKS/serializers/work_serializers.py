from rest_framework import serializers
from ..models.work_models import WorkStatusModel, WorkOrderStatusModel, WorkOrderModel


class WorkStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkStatusModel
        fields = "__all__"


class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrderModel
        fields = "__all__"


class WorkOrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrderStatusModel
        fields = "__all__"

