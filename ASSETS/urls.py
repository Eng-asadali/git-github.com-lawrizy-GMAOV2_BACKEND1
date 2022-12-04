"""gmao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import CompanyViewSet, UploadCompanyView, FacilityViewset, FloorViewSet, \
    RoomViewset, EquipmentViewset, EquipmentFamilyViewset, RoomTypeViewset, RoomTypeUploadView, RoomUploadView, \
    FloorUploadView
from rest_framework import routers
from django.urls import path

# pour les viewset on utilise router register
router = routers.SimpleRouter()
router.register(r'company', CompanyViewSet) # le r devant la chaine de caractère signifie raw, donc la chaine de
# caractere doit être traitée de manière brut
# sans gérer d'eventuels caractères d'echapement
router.register(r'facility', FacilityViewset)
router.register(r'floor', FloorViewSet)
router.register(r'room', RoomViewset)
router.register(r'equipment', EquipmentViewset)
router.register(r'equipment_family', EquipmentFamilyViewset)
router.register(r'room_type', RoomTypeViewset)


# pour les Apiview on utilise path
urlpatterns = [
    path('uploadCompany/', UploadCompanyView.as_view()),  # used for csv file batch
    path('room_type/room_type_upload/', RoomTypeUploadView.as_view()),  # used to upload room type csv
    path('room/room_upload/', RoomUploadView.as_view()),
    path('floor/floor_upload/', FloorUploadView.as_view())
]

urlpatterns += router.urls
