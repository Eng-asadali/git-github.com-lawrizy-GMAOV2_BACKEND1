from django_filters.rest_framework import DjangoFilterBackend

from ..models import JobTypeModel, JobModel, DomainModel
from rest_framework import viewsets, status, filters
from ..serializers import JobTypeSerializer, JobSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
import csv
from rest_framework.response import Response
from gmao.pagination import CustomPageNumberPagination


class JobTypeViewset(viewsets.ModelViewSet):
    queryset = JobTypeModel.objects.all()
    serializer_class = JobTypeSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['name', 'id']  # to filter by facility name or facility id
    ordering_fields = ['name', 'id']  # to order by facility name or facility id


class JobViewset(viewsets.ModelViewSet):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['domain_id', 'job_type_id','job','id']  # to filter by facility name or facility id
    ordering_fields = ['domain_id', 'job_type_id','job','id']  # to order by facility name or facility id

    def get_queryset(self):
        #print("Aziz request.query_params: ",self.request.query_params['domain_id'])
        queryset = JobModel.objects.all()
        return queryset



# la vue JobUploadView sert pour upload des batch d'intervention (ex: trop chaud...) au format csv
# le fichier csv contiendra 3 colonnes: job, domain, job_type
class JobUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication

    def post(self, request):
        content = request.data['file']    # we get the file from the request
        content = content.read().decode("utf8").split('\n')     # for csv.reader(), we need to split a string by line
        lines = csv.reader(content, delimiter=',')
        # print("AZIZ lines in file: ", lines)
        for line, i in zip(lines, range(len(content))):  # zip maps the 2 vectors per item -- i is used as counter
            if (i == 0) and ((line[0] != "job") or (line[1] != "domain") or (line[2] != "job_type")):
                # print("Aziz problem upload: ", line)
                content = {'upload job file': 'bad csv file structure'}
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)  # it means that the file is not good
            elif i != 0:  # exclude the header of the csv file
                #  print("AZIZ line content: ", line)
                a_job_type = JobTypeModel.objects.get(name=line[2])
                print(f"Aziz domain dans fichier {line[1]} -- numero line: {i+1}")
                a_domain = DomainModel.objects.get(name=line[1])
                a_job = JobModel(job=line[0], domain_id=a_domain, job_type_id=a_job_type)
                a_job.save()
            # print("AZIZ upload line numer done: ", i)
        content = {'upload job file': 'received and created'}
        return Response(content, status=status.HTTP_200_OK)

# JobPaginationViewset is used to paginate the JobModel queryset
class JobPaginationViewset(viewsets.ModelViewSet):
    queryset = JobModel.objects.all().order_by('id')
    serializer_class = JobSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['domain_id', 'job_type_id','job','id','domain_id__name','job_type_id__name']  # to filter by facility name or facility id
    ordering_fields = ['domain_id', 'job_type_id','job','id','domain_id__name','job_type_id__name']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to enable pagination

# JobTypePaginationViewset is used to paginate the JobTypeModel queryset
class JobTypePaginationViewset(viewsets.ModelViewSet):
    queryset = JobTypeModel.objects.all().order_by('id')
    serializer_class = JobTypeSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['name', 'id']  # to filter by facility name or facility id
    ordering_fields = ['name', 'id']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to enable pagination