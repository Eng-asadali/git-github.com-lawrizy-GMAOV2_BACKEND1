from .models import Company
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)  # to force the serializer to show the id

    class Meta:
        model = Company
        fields = '__all__'
