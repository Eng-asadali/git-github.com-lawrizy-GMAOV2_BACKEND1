from rest_framework import serializers
from ..models import RoomModel


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = RoomModel
        fields = '__all__'
        extra_kwargs = {
            'room': {'validators': []},  # on desactive les validators car quand on utilise RoomSerializer
            # comme nested serializer de WorkOrderSerializer dans le POST
            # le RoomSerializer.is_valid() est False car le validator dit
            # room doit etre unique
        }
