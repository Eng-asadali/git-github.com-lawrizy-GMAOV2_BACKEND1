from rest_framework import urls,routers
from .views import UserViewset
from rest_framework.authtoken import views
from django.urls import path
router = routers.SimpleRouter()
router.register(r'user', UserViewset)

urlpatterns = router.urls

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)    # this view is provided by DRF to get token for user
]
