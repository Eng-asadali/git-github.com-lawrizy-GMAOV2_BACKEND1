from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProfileSerializer
from .models import ProfileModel
# Create your views here.

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
