from rest_framework import viewsets
from ..serializers import DomainSerializer
from ..models import DomainModel


class DomainViewset(viewsets.ModelViewSet):
    serializer_class = DomainSerializer
    queryset = DomainModel.objects.all()