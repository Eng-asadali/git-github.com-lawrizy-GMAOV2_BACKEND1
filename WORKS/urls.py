from rest_framework import routers
from .views import DomainViewset, JobTypeViewset, JobViewset, WorkStatusViewset, WorkOrderViewset, \
    WorkOrderStatusViewset, DomainUploadView, JobUploadView
from django.urls import path

router = routers.SimpleRouter()
router.register(r'domain', DomainViewset)
router.register(r'job_type', JobTypeViewset)
router.register(r'job', JobViewset)
router.register(r'work_status', WorkStatusViewset)
router.register(r'work_order', WorkOrderViewset)
router.register(r'work_order_status', WorkOrderStatusViewset)

# pour les Apiview on utilise path
urlpatterns = [
    path('domain/domain_upload/', DomainUploadView.as_view()),  # used for csv file batch
    path('job/job_upload/', JobUploadView.as_view()),
]

urlpatterns += router.urls
