from rest_framework import routers
from .views import UserViewset,CurrentUserView, UserPaginationViewset
from rest_framework.authtoken import views
from django.urls import path

router = routers.SimpleRouter()
router.register(r'user', UserViewset)
router.register(r'user_pagination', UserPaginationViewset)

urlpatterns = router.urls

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token),    # this view is provided by DRF to get token for user
    path('current_user/', CurrentUserView.as_view())
]
