from ..models import Company
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False)  # on met le champs pour forcer l'affichage
                                                    # + read_only False pour qu'il ne soit pas exclu du **validated_data dans serializer.create()

    class Meta:
        model = Company
        fields = '__all__'
        extra_kwargs = {
            'company_name': {'validators': []}, # on desactive les validators car quand on utilise CompanySerializer
                                                # comme nested serializer de FacilitySerializer dans le POST
                                                # le FacilitySerializer.is_valid() est False car le validator dit
                                                # company_name doit etre unique
        }
