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
    #status : on rajoute le serializer pour pouvoir le nom du statut avec son nom dans liste des workorders
    status = WorkStatusSerializer(many=False, read_only=False)
    class Meta:
        model = WorkOrderModel
        fields = "__all__"

    # la methode doit être utilisée pour gérer l'objet status reçu lors de la création, car serializer imbriqué
    def create(self, validated_data):
        print("AZIZ validated_data: ", validated_data)
        status = validated_data.pop('status')  # on doit extraire le status car il est envoyé en objet complet
        status_id = status.pop("id")  # il faut faire pop pour extraire l'element dans ordered_dict
        status_obj = WorkStatusModel.objects.get(pk=status_id)
        new_wo = WorkOrderModel.objects.create(**validated_data, status=status_obj)
        return new_wo

    # la methode update doit doit être utilisée pour gérer l'objet status reçu lors de la création, car serializer imbriqué
    def update(self, instance, validated_data):
        # print(f"AZIZ instance: {type(instance)}")
        # print(f"AZIZ validate data: {validated_data}")
        wo_id = validated_data["id"]  #  on pourrait utilisé le parametre instance
        # print(f"AZIZ wo_id: {wo_id}")
        status = validated_data.pop('status')
        status_id = status.pop("id")  # il faut faire pop pour extraire l'element dans ordered_dict
        # print(f"AZIZ status_id: {status_id}")
        status_obj = WorkStatusModel.objects.get(pk=status_id)
        # print(f"AZIZ status_obj: {status_obj}")
        #  on met à jour le work order
        WorkOrderModel.objects.filter(pk=wo_id).update(**validated_data, status=status_obj)
        updated_wo = WorkOrderModel.objects.get(pk=wo_id)
        return updated_wo


class WorkOrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrderStatusModel
        fields = "__all__"

