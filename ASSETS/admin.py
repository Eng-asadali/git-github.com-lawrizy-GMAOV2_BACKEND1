from django.contrib import admin
from .models import Company
from .models import Facility
from .models import FloorModel
from .models import RoomModel
# Register your models here.

admin.site.register(Company)
admin.site.register(Facility)
admin.site.register(FloorModel)
admin.site.register(RoomModel)
