from rest_framework import serializers
from ..models import FloorModel


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FloorModel
        fields = '__all__'

