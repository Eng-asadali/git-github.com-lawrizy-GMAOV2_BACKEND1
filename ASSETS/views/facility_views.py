from rest_framework import viewsets
from ..models import Facility
from ..serializers import FacilitySerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status


# viewsets are easier than apiview because we don't have to define the methods
class FacilityViewset(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    #parser_classes = [MultiPartParser,FormParser]

    # la methode update permet d'intercepter la request et voir le contenu avant le serializer
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     print("AZIZ request.data: ", request.data)
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)

    # le partial update est utilisé pour un update dont on ne communique pas tous les champs = PATCH
    # le patch nécessite d'instancier un serializer avec 3 params: objet de la db à modifier + les données reçues du client + partial = true + ctxt
    # après il faut valider les données du serializer avec is_valid()
    # après il faut save()
    def partial_update(self, request, *args, **kwargs):
        #print("Aziz partial update request.data: ",request.data)
        current_facility = self.get_object()  # pour récupérer l'objet de la db
        #print("Aziz patch self.get_object: ",current_facility)
        serialized = FacilitySerializer(current_facility,request.data, partial=True,context={'request': request})
        #print("Aziz patch serialized: ",serialized)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_206_PARTIAL_CONTENT,data=serialized.data)
        else:
            print("Aziz patch error: ",serialized.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)

    # la methode get_serializer permet interception de la request avant traitement du serializer
    def get_serializer(self, *args, **kwargs):
        # leave this intact
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()

        print("AZZ get_serializer req: ",self.request.data)
        return serializer_class(*args, **kwargs)
