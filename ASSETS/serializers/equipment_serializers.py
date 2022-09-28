from rest_framework import serializers
from ..models import EquipmentModel, EquipmentFamilyModel

# Serializer for Equipment
class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquipmentModel
        fields = '__all__'


# Serializer for Equipment Family
class EquipmentFamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquipmentFamilyModel
        fields = '__all__'
