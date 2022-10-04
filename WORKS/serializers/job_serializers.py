from rest_framework import serializers
from ..models import JobTypeModel, JobModel


class JobTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = "__all__"


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = JobModel
