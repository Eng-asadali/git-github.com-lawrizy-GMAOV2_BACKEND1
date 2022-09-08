from django.db import models
from .company_models import Company


class Facility(models.Model):
    facility_name = models.CharField(max_length=500, null=False)
    street = models.CharField(max_length=500)
    number = models.IntegerField()
    postal_code = models.CharField(max_length=5)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    surface_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # ownership = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, related_name='facility') #related name is for request from company.facility
    image = models.ImageField(upload_to='pictures/facility') # upload_to is the folder where we store

    def __str__(self):
        return self.facility_name
