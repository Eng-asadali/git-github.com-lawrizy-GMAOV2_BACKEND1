from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from gmao.pagination import CustomPageNumberPagination
from ..models import Company
from ..serializers import CompanySerializer
from rest_framework.authentication import TokenAuthentication  # to use token authentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView  # used to manage the upload company file
from rest_framework.parsers import FormParser, MultiPartParser  # pour gerer upload fichier
from rest_framework.response import Response  # utilise pour la reponse
from rest_framework import status  # utilise pour renvoyer le code reponse
import csv  # utilisé pour lire le fichier company upload


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]   # to force authentication


# vue qui permet upload de societe
class UploadCompanyView(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        contenu = request.data['fichierCompany']    # we get the file from the request
        contenu = contenu.read().decode("utf8").split('\n')     # for csv.reader(), we need to split a string by line
        lines = csv.reader(contenu, delimiter=',')
        for line, i in zip(lines, range(len(contenu))):  # zip maps the 2 vectors per item -- i is used as counter
            if i != 0:  # exclude the header of the csv file
                a_company = Company(company_name=line[0], company_description=line[1])
                a_company.save()
        content = {'upload company file': 'received'}
        return Response(content, status=status.HTTP_200_OK)

class CompanyPaginationViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]   # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['company_name', 'id']  # to filter by facility name or facility id
    ordering_fields = ['company_name','id']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to set the pagination class