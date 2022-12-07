from rest_framework import serializers
from ..models.work_models import WorkStatusModel, WorkOrderStatusModel, WorkOrderModel


class WorkStatusSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage

    # + read_only False pour qu'il ne soit pas exclu du **validated_data dans serializer.create()
    # required False pour ne pas avoir besoin de l'envoyer à partir
    class Meta:
        model = WorkStatusModel
        fields = "__all__"


class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage
    # + read_only False pour qu'il ne soit pas exclu du **validated_data dans serializer.create()
    # required False pour ne pas avoir besoin de l'envoyer à partir

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

