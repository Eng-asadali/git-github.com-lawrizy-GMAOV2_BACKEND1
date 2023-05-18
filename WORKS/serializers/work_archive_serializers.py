from rest_framework import serializers

from ..models.work_archive_models import WorkOrderArchiveModel, WorkOrderStatusArchiveModel

class WorkOrderArchiveSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage
    # + read_only False pour qu'il ne soit pas exclu du **validated_data dans serializer.create()
    # required False pour ne pas avoir besoin de l'envoyer à partir

    # les champs date sont ajoutés pour précider qu'ils sont null pour
    # ..surcharger le fields all de la classe Meta
    creation_date = serializers.DateTimeField(required=False)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    #status : on rajoute le serializer pour pouvoir le nom du statut avec son nom dans liste des workorders
    #status = WorkStatusSerializer(many=False, read_only=False)
    status_read_only = serializers.CharField(source="status.name", read_only=True, required=False)
    # room serializer pour récupérer le nom complet
    #room = RoomSerializer(many=False, read_only=False)
    room_read_only = serializers.CharField(source='room.room', read_only=True, required=False)
    # assignee_read_only is a read only field used to display the assignee in the list of workorders
    reporter_read_only = serializers.CharField(source='reporter.username', read_only=True, required=False)
    assignee_read_only = serializers.CharField(source='assignee.username', read_only=True, required=False)
    # facility_read_only is a read only field used to display the facility in the list of workorders
    facility_read_only = serializers.CharField(source='room.floor.facility.facility_name', read_only=True, required=False)
    job_read_only = serializers.CharField(source='job.job', read_only=True, required=False)
    comment = serializers.CharField(required=False, allow_blank=True, allow_null=True) # used to comment to the workorder status history
    equipment_read_only = serializers.CharField(source='equipment.name', read_only=True, required=False)
    domain_read_only = serializers.CharField(source='domain.name', read_only=True, required=False)
    job_type_read_only = serializers.CharField(source='job_type.name', read_only=True, required=False)
    class Meta:
        model = WorkOrderArchiveModel
        fields = "__all__"

class WorkOrderStatusArchiveSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage
    work_order_id_read_only = serializers.CharField(source='work_order.id', read_only=True, required=False)
    status_before_read_only = serializers.CharField(source='status_before.name', read_only=True, required=False)
    status_after_read_only = serializers.CharField(source='status_after.name', read_only=True, required=False)
    author_read_only = serializers.CharField(source='author.username', read_only=True, required=False)

    class Meta:
        model = WorkOrderStatusArchiveModel
        fields = "__all__"
