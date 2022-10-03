from rest_framework import routers
from .views import DomainViewset, JobTypeViewset

router = routers.SimpleRouter()
router.register(r'domain', DomainViewset)
router.register(r'job_type', JobTypeViewset)

urlpatterns = router.urls
