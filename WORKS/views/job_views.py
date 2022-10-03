from ..models import JobTypeModel
from rest_framework import viewsets
from ..serializers import JobTypeSerializer


class JobTypeViewset(viewsets.ModelViewSet):
    queryset = JobTypeModel.objects.all()
    serializer_class = JobTypeSerializer
