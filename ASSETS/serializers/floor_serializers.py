from rest_framework import serializers
from ..models import FloorModel


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False, read_only=False)
    facility_read_only = serializers.CharField(source='facility.facility_name', read_only=True, required=False) #this is a read only field used to display the facility

    class Meta:
        model = FloorModel
        fields = '__all__'
