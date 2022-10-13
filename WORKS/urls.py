from rest_framework import routers
from .views import DomainViewset, JobTypeViewset, JobViewset, WorkStatusViewset, WorkOrderViewset, WorkOrderStatusViewset

router = routers.SimpleRouter()
router.register(r'domain', DomainViewset)
router.register(r'job_type', JobTypeViewset)
router.register(r'job', JobViewset)
router.register(r'work_status', WorkStatusViewset)
router.register(r'work_order', WorkOrderViewset)
router.register(r'work_order_status', WorkOrderStatusViewset)

urlpatterns = router.urls
