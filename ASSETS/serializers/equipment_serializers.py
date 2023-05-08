from rest_framework import serializers
from ..models import EquipmentModel, EquipmentFamilyModel

# Serializer for Equipment
class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)
    family_id_read_only = serializers.CharField(source='family_id.name', read_only=True, required=False) #this is a read only field used to display the equipment_family
    room_id_read_only = serializers.CharField(source='room_id.room', read_only=True, required=False) #this is a read only field used to display the room
    class Meta:
        model = EquipmentModel
        fields = '__all__'


# Serializer for Equipment Family
class EquipmentFamilySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)
    class Meta:
        model = EquipmentFamilyModel
        fields = '__all__'
