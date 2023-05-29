import csv

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from gmao.pagination import CustomPageNumberPagination
from ..serializers import EquipmentFamilySerializer, EquipmentSerializer
from ..models import EquipmentModel, EquipmentFamilyModel, RoomModel
from django_filters.rest_framework import DjangoFilterBackend # to filter the queryset
from rest_framework import filters # to filter the queryset
from rest_framework.response import Response


class EquipmentViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = EquipmentModel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room_id','family_id','id']  # to filter by facility name or facility id
    ordering_fields = ['room_id','family_id','id']  # to order by facility name or facility id


class EquipmentFamilyViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentFamilySerializer
    queryset = EquipmentFamilyModel.objects.all()

# EquipmentPaginationViewSet is used to paginate the queryset
class EquipmentPaginationViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = EquipmentModel.objects.all().order_by('id') # to order the queryset for pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['room_id','id','family_id','name','room_id__room']  # to filter by facility name or facility id
    ordering_fields = ['room_id','id','family_id','name','room_id__room']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to set the pagination class

#EquipmentFamilyPaginationViewset is used to paginate the queryset
class EquipmentFamilyPaginationViewset(viewsets.ModelViewSet):
    serializer_class = EquipmentFamilySerializer
    queryset = EquipmentFamilyModel.objects.all().order_by('id') # to order the queryset for pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['id','parent_id','parent_id__name','name']  # to filter by facility name or facility id
    ordering_fields = ['id','parent_id','parent_id__name','name']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to set the pagination class

#EquipmentFamilyUploadView is used to upload a csv file  with family to the database
class EquipmentFamilyUploadApiView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    def post(self, request):
        content = request.data['file']  # we get the file from the request
        content = content.read().decode("utf8").split('\n')  # for csv.reader(), we need to split a string by line
        lines = csv.reader(content, delimiter=',')
        # print("AZIZ lines in file: ", lines)
        for line, i in zip(lines, range(len(content))):  # zip maps the 2 vectors per item -- i is used as counter
            #check if the header of the csv file is NOT correct
            if (i == 0) and ((line[0] != "name") or (line[1] != "description") or (line[2] != "parent_id")):
                # print("Aziz proble upload: ", line)
                content = {'upload room file': 'bad csv file structure'}
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)  # it means that the file is not good
            elif i != 0:  # exclude the header of the csv file
                #if the line contains a parent_id, we create a room with a parent_id
                if line[2] != "":
                    a_parent_id = EquipmentFamilyModel.objects.get(id=line[2])
                else:
                    a_parent_id = None
                a_family_eqp = EquipmentFamilyModel(name=line[0], description=line[1], parent_id=a_parent_id)
                a_family_eqp.save()
                # print("AZIZ upload done: ",line)
        content = {'upload family eqp file': 'received and created'}
        return Response(content, status=status.HTTP_200_OK)

#EquipmentUploadView is used to upload a csv file  equipment to the database
class EquipmentUploadApiView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication

    def post(self, request):
        content = request.data['file']  # we get the file from the request
        content = content.read().decode("utf8").split('\n')  # for csv.reader(), we need to split a string by line
        lines = csv.reader(content, delimiter=',')
        # print("AZIZ lines in file: ", lines)
        for line, i in zip(lines, range(len(content))):  # zip maps the 2 vectors per item -- i is used as counter
            # check if the header of the csv file is NOT correct
            if (i == 0) and ((line[0] != "name") or (line[1] != "description") or (line[2] != "parent_id") or (line[3] != "room_id") or (line[4] != "family_id")):
                # print("Aziz proble upload: ", line)
                content = {'upload room file': 'bad csv file structure'}
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)  # it means that the file is not good
            elif i != 0:  # exclude the header of the csv file
                # if the line contains a parent_id, we create a room with a parent_id
                if line[2] != "":
                    a_parent_id = EquipmentFamilyModel.objects.get(id=line[2])
                else:
                    a_parent_id = None
                a_room_id = RoomModel.objects.get(id=line[3])
                a_family_id = EquipmentFamilyModel.objects.get(id=line[4])

                an_eqp = EquipmentModel(name=line[0], description=line[1], parent_id=a_parent_id, room_id=a_room_id, family_id=a_family_id)
                an_eqp.save()
                # print("AZIZ upload done: ",line)
        content = {'upload eqp file': 'received and created'}
        return Response(content, status=status.HTTP_200_OK)