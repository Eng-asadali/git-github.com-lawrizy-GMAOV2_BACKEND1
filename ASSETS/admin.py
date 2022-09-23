from django.contrib import admin
from .models import Company
from .models import Facility
from .models import FloorModel
# Register your models here.

admin.site.register(Company)
admin.site.register(Facility)
admin.site.register(FloorModel)
