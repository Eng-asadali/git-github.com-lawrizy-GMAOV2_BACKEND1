from rest_framework import viewsets, status, filters

from gmao.pagination import CustomPageNumberPagination  # to set the pagination class
from ..serializers import FloorSerializer
from ..models import FloorModel, Facility
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
import csv
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend # to filter the queryset


class FloorViewSet(viewsets.ModelViewSet):
    queryset = FloorModel.objects.all()
    serializer_class = FloorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # to filter the queryset
    filterset_fields = ['facility__facility_name', 'id', 'facility'] # to filter by facility name or facility id
    ordering_fields = ['facility__facility_name', 'id', 'facility'] # to order by facility name or facility id


# la vue RoomUploadView sert pour upload des batch de room au format csv
class FloorUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser]  # Multipartparser is for the uploaded files
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication

    def post(self, request):
        content = request.data['file']    # we get the file from the request
        content = content.read().decode("utf8").split('\n')     # for csv.reader(), we need to split a string by line
        lines = csv.reader(content, delimiter=',')
        print("AZIZ lines in file: ", lines)
        for line, i in zip(lines, range(len(content))):  # zip maps the 2 vectors per item -- i is used as counter
            if (i == 0) and ((line[0] != "facility") or (line[1] != "floor")):
                # print("Aziz proble upload: ", line)
                content = {'upload company file': 'bad csv file structure'}
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)  # it means that the file is not good
            elif i != 0:  # exclude the header of the csv file
                #  print("AZIZ line content: ", line)
                a_facility = Facility.objects.get(facility_name=line[0])
                a_floor = FloorModel(floor=line[1], facility=a_facility)
                a_floor.save()
                # print("AZIZ upload done: ",line)
        content = {'upload company file': 'received and created'}
        return Response(content, status=status.HTTP_200_OK)

class FloorPaginationViewSet(viewsets.ModelViewSet):
    queryset = FloorModel.objects.all().order_by('id') #we need to order the queryset by id to use pagination
    serializer_class = FloorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # to filter the queryset
    filterset_fields = ['facility__facility_name', 'id', 'facility'] # to filter by facility name or facility id
    ordering_fields = ['facility__facility_name', 'id', 'facility'] # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination # to set the pagination class