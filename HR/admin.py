from django.contrib import admin
from .models import ProfileModel
from rest_framework.authtoken.admin import TokenAdmin  # to be able to manage token for users

# Register your models here.
admin.site.register(ProfileModel)

TokenAdmin.raw_id_fields = ['user']  # to be able to manage token for users
