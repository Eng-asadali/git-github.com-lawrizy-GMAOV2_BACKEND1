from django.db import models


# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255, unique=True, null=False)
    company_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.company_name
