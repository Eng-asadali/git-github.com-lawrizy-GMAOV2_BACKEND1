from ..models import JobTypeModel, JobModel
from rest_framework import viewsets
from ..serializers import JobTypeSerializer, JobSerializer


class JobTypeViewset(viewsets.ModelViewSet):
    queryset = JobTypeModel.objects.all()
    serializer_class = JobTypeSerializer


class JobViewset(viewsets.ModelViewSet):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
