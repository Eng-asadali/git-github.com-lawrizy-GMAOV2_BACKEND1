from ..models import JobTypeModel, JobModel
from rest_framework import viewsets
from ..serializers import JobTypeSerializer, JobSerializer
from django_filters.rest_framework import DjangoFilterBackend


class JobTypeViewset(viewsets.ModelViewSet):
    queryset = JobTypeModel.objects.all()
    serializer_class = JobTypeSerializer


class JobViewset(viewsets.ModelViewSet):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
    #filter_backends = [DjangoFilterBackend] # permet de faire du generic filtering avec la library django-filter
    #filterset_fieds = ('domain_id') #it is an array with the list of filter field

    def get_queryset(self):
        print("Aziz request.query_params: ",self.request.query_params['domain_id'])
        queryset = JobModel.objects.all()
        return queryset


