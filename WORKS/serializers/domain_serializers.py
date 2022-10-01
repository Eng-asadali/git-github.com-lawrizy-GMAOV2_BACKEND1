from rest_framework import serializers
from ..models import DomainModel


class DomainSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DomainModel
        fields = '__all__'
