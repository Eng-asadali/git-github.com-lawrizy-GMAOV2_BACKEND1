from rest_framework import serializers
from ..models.work_models import WorkStatusModel, WorkOrderStatusModel, WorkOrderModel


class WorkStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkStatusModel
        fields = "__all__"


class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    # les champs date sont ajoutés pour précider qu'ils sont null pour
    # ..surcharger le fields all de la classe Meta
    creation_date = serializers.DateTimeField(required=False)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    class Meta:
        model = WorkOrderModel
        fields = "__all__"



class WorkOrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrderStatusModel
        fields = "__all__"

