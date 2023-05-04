from rest_framework import serializers
from ..models import JobTypeModel, JobModel


class JobTypeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage

    # + read_only False pour qu'il ne soit pas exclu du **validated_data dans serializer.create()
    # required False pour ne pas avoir besoin de l'envoyer à partir
    class Meta:
        model = JobTypeModel
        fields = "__all__"


class JobSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage
    domain_id_read_only = serializers.CharField(source='domain_id.name', read_only=True, required=False)
    job_type_id_read_only = serializers.CharField(source='job_type_id.name', read_only=True, required=False)

    # + read_only False pour qu'il ne soit pas exclu du **validated_data dans serializer.create()
    # required False pour ne pas avoir besoin de l'envoyer à partir
    class Meta:
        fields = '__all__'
        model = JobModel
