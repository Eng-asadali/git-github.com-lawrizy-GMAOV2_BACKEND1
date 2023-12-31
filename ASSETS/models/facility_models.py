from django.db import models
from .company_models import Company


class Facility(models.Model):
    facility_name = models.CharField(max_length=500, null=False)
    street = models.CharField(max_length=500, null=True)
    number = models.CharField(null=True,max_length=10)
    postal_code = models.CharField(max_length=5, null=True)
    locality = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    surface_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # ownership = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, related_name='facility') #related name is for request from company.facility
    image = models.ImageField(upload_to='media/pictures/facility', null=True) # upload_to is the folder where we store

    class Meta:
        constraints = [models.UniqueConstraint(fields=['company', 'facility_name'], name='uniqueConst_1_facility_per_company')]

    def __str__(self):
        return self.facility_name

