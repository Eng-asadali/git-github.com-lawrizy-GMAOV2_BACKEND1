from rest_framework import routers
from .views import DomainViewset, JobTypeViewset, JobViewset, WorkStatusViewset, WorkOrderViewset, \
    WorkOrderStatusViewset, DomainUploadView, JobUploadView, WorkOrderPictureViewset, DomainPaginationViewset, \
    JobPaginationViewset, JobTypePaginationViewset, WorkOrderPaginationViewset, WorkOrderArchivePaginationViewset, \
    WorkOrderStatusArchivePaginationViewset, WorkOrderHourPaginationViewset, WorkStatusPaginationViewset, \
    JobEquipmentUploadView, CreatePreventiveWo, DeletePreventiveWo
from django.urls import path

router = routers.SimpleRouter()
router.register(r'domain', DomainViewset)
router.register(r'domain_pagination', DomainPaginationViewset)
router.register(r'job_type', JobTypeViewset)
router.register(r'job_type_pagination', JobTypePaginationViewset)
router.register(r'job', JobViewset)
router.register(r'job_pagination', JobPaginationViewset)
router.register(r'work_status', WorkStatusViewset)
router.register(r'work_status_pagination', WorkStatusPaginationViewset)
router.register(r'work_order', WorkOrderViewset)
router.register(r'work_order_pagination', WorkOrderPaginationViewset)
router.register(r'work_order_archive_pagination', WorkOrderArchivePaginationViewset)
router.register(r'work_order_status_archive_pagination', WorkOrderStatusArchivePaginationViewset)
router.register(r'work_order_status', WorkOrderStatusViewset)
router.register(r'work_order_picture', WorkOrderPictureViewset)
router.register(r'work_order_hour_pagination', WorkOrderHourPaginationViewset)

# pour les Apiview on utilise path
urlpatterns = [
    path('domain/domain_upload/', DomainUploadView.as_view()),  # used for csv file batch
    path('job/job_upload/', JobUploadView.as_view()),
    path('job/job_equipment_upload/', JobEquipmentUploadView.as_view()),
    path('job/create_preventive_wo/', CreatePreventiveWo.as_view()),
    path('delete_preventive_wo/', DeletePreventiveWo.as_view()),
]

urlpatterns += router.urls
