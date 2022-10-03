from rest_framework import serializers
from ..models import JobTypeModel


class JobTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JobTypeModel
        fields = "__all__"
