from rest_framework import viewsets,status
from ..serializers import FloorSerializer
from ..models import FloorModel
from rest_framework.response import Response


class FloorViewSet(viewsets.ModelViewSet):
    queryset = FloorModel.objects.all()
    serializer_class = FloorSerializer

    # def partial_update(self, request, *args, **kwargs):
    #     serializer = FloorSerializer(self.get_object(),request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
    #     else:
    #         Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)
