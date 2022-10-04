from rest_framework import routers
from .views import DomainViewset, JobTypeViewset, JobViewset

router = routers.SimpleRouter()
router.register(r'domain', DomainViewset)
router.register(r'job_type', JobTypeViewset)
router.register(r'job',JobViewset)

urlpatterns = router.urls
