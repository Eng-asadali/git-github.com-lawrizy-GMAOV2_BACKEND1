from rest_framework import serializers
from ..models.facility_models import *
from .company_serializers import CompanySerializer


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    # we have to force the serializers to allow null and blank even if defined in model
    id = serializers.IntegerField(required=False, read_only=False)
    city = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    locality = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    number = serializers.CharField(allow_null=True, required=False,allow_blank=True)
    postal_code = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    image = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False)
    company = CompanySerializer(many=False, read_only=False) # CompanySerializer est utilisé pour récupérer
                                                            # pas uniquement l'id (hyperlinked) mais aussi les champs text du model
    company_read_only = serializers.CharField(source='company.company_name', read_only=True, required=False) #this is a read only field used to display the company


    class Meta:
        model = Facility
        fields = '__all__'

    # la methode create est appelle lors du serializer.save() au niveau
    # du FacilityViewset quand le serializer a été construit juste avec un param: request.data
    def create(self, validated_data):
        #print("Aziz validated_data: ", validated_data)
        company_id = validated_data["company"]["id"]
        #print("Aziz company_id: ", company_id)

        # dans la ligne suivante, on fait un pop car lors de la création du facility à la ligne 32
        # on donne deja la company en premier parametre
        # sinon il y aura de la redondance
        print("Aziz validated_data.pop: ", validated_data.pop("company"))
        company = Company.objects.get(pk=company_id)
        #print("Aziz company.get: ",company)
        facility = Facility.objects.create(company=company, **validated_data)
        #print("Aziz facility created: ",facility)
        return facility

    # la methode update est appelle lors du serializer.save() au niveau
    # du FacilityViewset.partial_update() quand le serializer a été construit juste avec
    # 2 param: request.data + instance
    def update(self, instance, validated_data):
        print("facility_serial instance: ", instance)
        print("facility_serial validated_date: ", validated_data)
        facility_id = validated_data["id"]
        company_id = validated_data["company"]["id"]
        validated_data.pop("company") #il faut enlever ce champ du dictionnaire pour pouvoir faire la mise à jour
        Facility.objects.filter(pk=facility_id).update(**validated_data) #on met à jour les champs du dictionnaire
        Facility.objects.filter(pk=facility_id).update(company=company_id) #on met à jour la clé étrangère de la société
        facility = Facility.objects.get(pk=facility_id) #on récupère l'objet pour réponse
        print("facility after update: ", facility)
        return facility
