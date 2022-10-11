from rest_framework import urls,routers
from .views import UserViewset

router = routers.SimpleRouter()
router.register(r'user', UserViewset)

urlpatterns = router.urls
