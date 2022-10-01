from rest_framework import routers
from .views import DomainViewset

router = routers.SimpleRouter()
router.register(r'domain', DomainViewset)

urlpatterns = router.urls