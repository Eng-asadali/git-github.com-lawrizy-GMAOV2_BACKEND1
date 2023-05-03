from rest_framework import routers
from .views import DomainViewset, JobTypeViewset, JobViewset, WorkStatusViewset, WorkOrderViewset, \
    WorkOrderStatusViewset, DomainUploadView, JobUploadView, WorkOrderPictureViewset, DomainPaginationViewset, \
    JobPaginationViewset, JobTypePaginationViewset, WorkOrderPaginationViewset, WorkOrderArchivePaginationViewset, \
    WorkOrderStatusArchivePaginationViewset
from django.urls import path

router = routers.SimpleRouter()
router.register(r'domain', DomainViewset)
router.register(r'domain_pagination', DomainPaginationViewset)
router.register(r'job_type', JobTypeViewset)
router.register(r'job_type_pagination', JobTypePaginationViewset)
router.register(r'job', JobViewset)
router.register(r'job_pagination', JobPaginationViewset)
router.register(r'work_status', WorkStatusViewset)
router.register(r'work_order', WorkOrderViewset)
router.register(r'work_order_pagination', WorkOrderPaginationViewset)
router.register(r'work_order_archive_pagination', WorkOrderArchivePaginationViewset)
router.register(r'work_order_status_archive_pagination', WorkOrderStatusArchivePaginationViewset)
router.register(r'work_order_status', WorkOrderStatusViewset)
router.register(r'work_order_picture', WorkOrderPictureViewset)

# pour les Apiview on utilise path
urlpatterns = [
    path('domain/domain_upload/', DomainUploadView.as_view()),  # used for csv file batch
    path('job/job_upload/', JobUploadView.as_view()),
]

urlpatterns += router.urls
