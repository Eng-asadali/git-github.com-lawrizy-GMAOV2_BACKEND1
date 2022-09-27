from rest_framework import serializers
from ..models.facility_models import *
from .company_serializers import CompanySerializer


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    # we have to force the serializers to allow null and blank even if defined in model
    city = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    locality = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    number = serializers.CharField(allow_null=True, required=False,allow_blank=True)
    postal_code = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    image = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False)
    company = CompanySerializer(many=False, read_only=False) # CompanySerializer est utilisé pour récupérer
                                                            # pas uniquement l'id (hyperlinked) mais aussi les champs text du model

    class Meta:
        model = Facility
        fields = '__all__'

    # la methode create est appelle lors du serializer.save() au niveau
    # du FacilityViewset quand le serializer a été construit juste avec un param: request.data
    def create(self, validated_data):
        print("Aziz validated_data: ", validated_data)
        company_id = validated_data["company"]["id"]
        print("Aziz company_id: ", company_id)
        print("Aziz validated_data.pop: ", validated_data.pop("company"))
        company = Company.objects.get(pk=company_id)
        facility = Facility.objects.create(company=company, **validated_data)
        return facility
