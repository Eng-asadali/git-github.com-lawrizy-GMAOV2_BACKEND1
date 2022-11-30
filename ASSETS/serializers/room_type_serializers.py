from rest_framework import serializers
from ..models import RoomTypeModel


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RoomTypeModel
        fields = '__all__'
