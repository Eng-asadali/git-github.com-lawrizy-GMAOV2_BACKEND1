from rest_framework import serializers
from ..models.facility_models import *


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    # we have to force the serializers to allow null and blank even if defined in model
    city = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    locality = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    number = serializers.CharField(allow_null=True, required=False,allow_blank=True)
    postal_code = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    image = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False)

    class Meta:
        model = Facility
        fields = '__all__'
