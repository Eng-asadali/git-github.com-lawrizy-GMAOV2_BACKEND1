from rest_framework import viewsets, status
from ..serializers import RoomSerializer
from ..models import RoomModel, RoomTypeModel, FloorModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
import csv
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend # to filter the queryset
from rest_framework import filters # to filter the queryset
from gmao.pagination import CustomPageNumberPagination  # to set the pagination class


class RoomViewset(viewsets.ModelViewSet):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['floor', 'room_type']  # to filter by floor name or room_type id
    ordering_fields = ['floor', 'room_type']  # to order by floor name or room_type id


# la vue RoomUploadView sert pour upload des batch de room au format csv
class RoomUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication

    def post(self, request):
        content = request.data['file']    # we get the file from the request
        content = content.read().decode("utf8").split('\n')     # for csv.reader(), we need to split a string by line
        lines = csv.reader(content, delimiter=',')
        # print("AZIZ lines in file: ", lines)
        for line, i in zip(lines, range(len(content))):  # zip maps the 2 vectors per item -- i is used as counter
            if (i == 0) and ((line[0] != "floor") or (line[1] != "room")or (line[2] != "room_type")):
                # print("Aziz proble upload: ", line)
                content = {'upload room file': 'bad csv file structure'}
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)  # it means that the file is not good
            elif i != 0:  # exclude the header of the csv file
                #  print("AZIZ line content: ", line)
                a_room_type = RoomTypeModel.objects.get(room_type=line[2])
                a_floor = FloorModel.objects.get(floor=line[0])
                a_room = RoomModel(room=line[1], room_type=a_room_type, floor=a_floor)
                a_room.save()
                # print("AZIZ upload done: ",line)
        content = {'upload company file': 'received and created'}
        return Response(content, status=status.HTTP_200_OK)

# RoomPaginationViewset is used to paginate the room queryset
class RoomPaginationViewset(viewsets.ModelViewSet):
    queryset = RoomModel.objects.all().order_by('id') # to order the queryset for pagination
    serializer_class = RoomSerializer
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['floor', 'room_type','id','room','floor__floor','room_type__room_type','floor__facility__facility_name']  # to filter by floor name or room_type id
    ordering_fields = ['floor', 'room_type','id','room','floor__floor','room_type__room_type','floor__facility__facility_name']  # to order by floor name or room_type id
    pagination_class = CustomPageNumberPagination  # to set the pagination class