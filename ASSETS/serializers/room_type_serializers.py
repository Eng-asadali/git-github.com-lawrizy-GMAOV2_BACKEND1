from rest_framework import serializers
from ..models import RoomTypeModel


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = RoomTypeModel
        fields = '__all__'
