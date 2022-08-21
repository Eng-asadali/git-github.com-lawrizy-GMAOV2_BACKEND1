from rest_framework import viewsets
from ..models import Facility
from ..serializers import FacilitySerializer


# viewsets are easier than apiview because we don't have to define the methods
class FacilityViewset(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
