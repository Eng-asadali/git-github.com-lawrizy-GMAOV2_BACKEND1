from rest_framework import serializers
from ..models.facility_models import *


class FacilitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Facility
        fields = '__all__'
