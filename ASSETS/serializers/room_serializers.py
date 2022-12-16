from rest_framework import serializers
from ..models import RoomModel


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)
    room_type_read_only = serializers.CharField(source='room_type.room_type', read_only=True, required=False) #this is a read only field used to display the room_type

    class Meta:
        model = RoomModel
        fields = '__all__'
        extra_kwargs = {
            'room': {'validators': []},  # on desactive les validators car quand on utilise RoomSerializer
            # comme nested serializer de WorkOrderSerializer dans le POST
            # le RoomSerializer.is_valid() est False car le validator dit
            # room doit etre unique
        }
