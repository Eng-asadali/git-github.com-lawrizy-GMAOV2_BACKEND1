from rest_framework import serializers
from ..models import RoomModel


class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RoomModel
        fields = '__all__'

