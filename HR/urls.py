from rest_framework import urls,routers
from .views import ProfileViewset

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewset)

urlpatterns = router.urls
