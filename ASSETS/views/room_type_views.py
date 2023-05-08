from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from gmao.pagination import CustomPageNumberPagination
from ..serializers import RoomTypeSerializer
from ..models import RoomTypeModel
import csv


class RoomTypeViewset(viewsets.ModelViewSet):
    queryset = RoomTypeModel.objects.all()
    serializer_class = RoomTypeSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    ordering_fields = ['room_type']


#cette classe est utilisé pour import du fichier csv
class RoomTypeUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication

    def post(self, request):
        contenu = request.data['fichier']    # we get the file from the request
        contenu = contenu.read().decode("utf8").split('\n')     # for csv.reader(), we need to split a string by line
        lines = csv.reader(contenu, delimiter=',')
        print("AZIZ lines in file: ",lines)
        for line, i in zip(lines, range(len(contenu))):  # zip maps the 2 vectors per item -- i is used as counter
            if (i == 0) and ((line[0] != "room_type") or (line[1] != "code")):
                print("Aziz proble upload: ", line)
                content = {'upload company file': 'bad csv file structure'}
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)  # it means that the file is not good
            elif i != 0:  # exclude the header of the csv file
                a_room_type = RoomTypeModel(room_type=line[0], code=line[1])
                a_room_type.save()
                print("AZIZ upload done: ",line)
        content = {'upload company file': 'received and created'}
        return Response(content, status=status.HTTP_200_OK)

# RoomTypePaginationViewset is used to paginate the queryset
class RoomTypePaginationViewset(viewsets.ModelViewSet):
    queryset = RoomTypeModel.objects.all().order_by('id') #we need to order the queryset by id to use pagination
    serializer_class = RoomTypeSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room_type', 'code']  # to filter by facility name or facility id
    ordering_fields = ['room_type','code']
    pagination_class = CustomPageNumberPagination # to set the pagination class