from rest_framework import viewsets
from ..models import Facility
from ..serializers import FacilitySerializer
from rest_framework.response import Response


# viewsets are easier than apiview because we don't have to define the methods
class FacilityViewset(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    # la methode update permet d'intercepter la request et voir le contenu avant le serializer
    def update(self, request, *args, **kwargs):
        #print("AZIZ request.data: ",request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # la methode get_serializer permet interception de la request avant traitement du serializer
    def get_serializer(self, *args, **kwargs):
        # leave this intact
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()

        #print("AZZ req: ",self.request.data)
        return serializer_class(*args, **kwargs)