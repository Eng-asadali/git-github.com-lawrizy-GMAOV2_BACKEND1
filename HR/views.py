from rest_framework import viewsets
from .serializer import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
