from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.views import APIView

from gmao.pagination import CustomPageNumberPagination
from .serializer import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# UserViewSet est utilisé pour afficher les users et leurs groupes associés
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# CurrentUser apiview est utilisé pour afficher le user courant et ses groupes associés
# CurrentUser needs authentication and permission to extract the current user from the request
class CurrentUserView(APIView):
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    def get(self, request):
        #print(f"request: {request} -- request.user: {request.user}")
        context = {'request': request}
        serializer = UserSerializer(request.user, context=context)
        return Response(serializer.data)

class UserPaginationViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    authentication_classes = [TokenAuthentication]  # to use token authentication
    permission_classes = [IsAuthenticated]  # to force authentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # to filter the queryset
    filterset_fields = ['username', 'id','email','first_name']  # to filter by facility name or facility id
    ordering_fields = ['username', 'id','email','last_name']  # to order by facility name or facility id
    pagination_class = CustomPageNumberPagination  # to use our custom pagination