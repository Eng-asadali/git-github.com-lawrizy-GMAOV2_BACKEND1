from django.contrib.auth.models import User
from rest_framework import serializers

from django.conf import settings

from ..models.work_models import WorkStatusModel, WorkOrderStatusModel, WorkOrderModel, WorkOrderPictureModel
from ASSETS.serializers.room_serializers import RoomSerializer
from ASSETS.models.room_models import RoomModel
from django.core.mail import send_mail


class WorkStatusSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage

    # + read_only False pour qu'il ne soit pas exclu du **validated_data dans serializer.create()
    # required False pour ne pas avoir besoin de l'envoyer à partir
    class Meta:
        model = WorkStatusModel
        fields = "__all__"


class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
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
        model = WorkOrderModel
        fields = "__all__"

    # la methode doit être utilisée pour gérer l'objet status reçu lors de la création, car serializer imbriqué
    # def create(self, validated_data):
    #     print("AZIZ validated_data: ", validated_data)
    #     status = validated_data.pop('status')  # on doit extraire le status car il est envoyé en objet complet
    #     status_id = status.pop("id")  # il faut faire pop pour extraire l'element dans ordered_dict
    #     status_obj = WorkStatusModel.objects.get(pk=status_id)
    #     room = validated_data.pop('room')
    #     room_id = room.pop("id")
    #     room_obj = RoomModel.objects.get(pk=room_id)
    #     print(f"AZIZ room_obj: {room_obj}")
    #     new_wo = WorkOrderModel.objects.create(**validated_data, status=status_obj, room=room_obj)
    #     return new_wo

    # la methode update doit doit être utilisée pour gérer l'objet status reçu lors de la création, car serializer imbriqué
    # update est utilisé lors du changement de status du workorder
    # update est utilisé lors du changement du responsable du workorder
    def update(self, instance, validated_data):
        # get the current user to set it as the author of the status change
        current_user = self.context['request'].user

        # check if the assignee received is different from the current assignee - if yes, we record the event
        new_assignee = validated_data.get('assignee', None)
        if (new_assignee != instance.assignee) and (new_assignee is not None):
            # we create a new record in the WorkOrderStatusModel
            WorkOrderStatusModel.objects.create(status_before=instance.status, status_after=instance.status,
                                                work_order=instance, author=current_user, comment="changement de responsable")
            instance.assignee = new_assignee
            instance.save()

        # we check if the status received is different from the current status
        if instance.status != validated_data.get('status', instance.status):
            # we create a new record in the WorkOrderStatusModel
            new_status = validated_data.get('status', instance.status)
            # record the event in the WorkOrderStatusModel
            WorkOrderStatusModel.objects.create(status_before=instance.status, status_after=new_status,
                                                work_order=instance, author=current_user, comment="changement de status")
            # update the status of the work order
            instance.status = validated_data.get('status', instance.status)
            instance.save()

        # we check if we received a new comment - if yes we record it in the WorkOrderStatusModel with the current status
        new_comment = validated_data.get('comment', None) # retrieve the value of the 'comment' key in the validated_data dictionary if it exists else None
        if (new_comment is not None) and (new_comment != ""):
            WorkOrderStatusModel.objects.create(status_before=instance.status, status_after=instance.status,
                                                work_order=instance, author=current_user, comment=new_comment)
            instance.save()

        # we send email to the assignee
        # we get the assignee email if it exists
        if (instance.assignee is not None) and (instance.assignee.email is not None):
            email_to = instance.assignee.email
            email_subject = f"Ordre de travail {instance.id} mis à jour"
            email_body = f"Numéro ordre travail: {instance.id}\nResponsable: {instance.assignee.username},\n" \
                         f"Nouveau status: {instance.status}\nAuteur du changement: {current_user.username}\n"
            email_from = settings.EMAIL_HOST_USER
            send_mail(
                email_subject,
                email_body,
                email_from,
                [email_to],
            )
        return instance
    # add a method to override the create method: to send an email to the assignee, the reporter and the users of the admin group
    def create(self, validated_data):
        # we create the work order
        new_wo = WorkOrderModel.objects.create(**validated_data)
        # create an array of emails of the users of the admin group
        emails_to = []
        for user in User.objects.filter(groups__name='admin'):
            emails_to.append(user.email)
        # check if the reporter email and the assignee email exists and add to the array
        if new_wo.reporter is not None:
            emails_to.append(new_wo.reporter.email)
        if new_wo.assignee is not None:
            emails_to.append(new_wo.assignee.email)
        # we send the email
        email_subject = f"Nouvel ordre de travail {new_wo.id}"
        email_body = f"Numéro ordre travail: {new_wo.id}\nRapporteur: {new_wo.reporter.username},\n" \
                     f"Status: {new_wo.status}\nLocal: {new_wo.room.room},\n" \
                     f"Intervention: {new_wo.job.job},\n"
        email_from = settings.EMAIL_HOST_USER
        send_mail(
            email_subject,
            email_body,
            email_from,
            emails_to,
        )
        return new_wo


#WorkOrderStatusSerializer is used to display the status history of a work order
class WorkOrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage
    work_order_id_read_only = serializers.CharField(source='work_order.id', read_only=True, required=False)
    status_before_read_only = serializers.CharField(source='status_before.name', read_only=True, required=False)
    status_after_read_only = serializers.CharField(source='status_after.name', read_only=True, required=False)
    author_read_only = serializers.CharField(source='author.username', read_only=True, required=False)

    class Meta:
        model = WorkOrderStatusModel
        fields = "__all__"


#a serializer for the WorkOrderPictureModel that is used to upload pictures
class WorkOrderPictureSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)  # on met le champs pour forcer l'affichage
    work_order_id_read_only = serializers.CharField(source='work_order.id', read_only=True, required=False)
    class Meta:
        model = WorkOrderPictureModel
        fields = "__all__"

