# pagination.py
# AZIZ: used by specif viewsets to set the number of items per page
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20  # Set the number of items per page