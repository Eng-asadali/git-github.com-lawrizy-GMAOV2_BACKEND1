from django.contrib import admin
from .models import DomainModel, JobTypeModel, JobModel

# Register your models here.
admin.site.register(DomainModel)
admin.site.register(JobTypeModel)
admin.site.register(JobModel)

