from rest_framework import serializers
from .models import ProfileModel
from django.contrib.auth.models import User, Group

# on a besoin du GroupSerializer car il sera utilisé par le UserSerializer pour afficher les groupes associés à un user
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


# UserSerializer est utilisé pour afficher les users et leurs groupes associés
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # id: to force the display of the id field
    id = serializers.IntegerField(read_only=False, required=False)
    groups = GroupSerializer(many=True, required=False)
    #add password field to make it not required
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    class Meta:
        model = User
        fields = '__all__'

    # la methode create() est utilisée car le password doit être hasché
    def create(self, validated_data):
        print("Aziz validated_data",validated_data)
        user = User.objects.create_user(username=validated_data["username"],password=validated_data["password"])
        user.save()
        return user

    #implementé de manière à mettre uniquement le password et email  et username à jour
    def update(self, instance, validated_data):
        # print("instance: ", type(instance))
        # user = User.objects.get(username=instance)
        #print("AZIZ update user: ", instance.username)
        if ("password" in validated_data) and (validated_data["password"] != ""):
            instance.set_password(raw_password=validated_data["password"])
            instance.save()
        instance.username = validated_data["username"]
        instance.email = validated_data["email"]    # to update the email
        instance.save()
        #print("AZIZ update user DONE")
        return instance


# ProfileSerializer n'est pas utilisé actuellement
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password')
    class Meta:
        model = ProfileModel
        fields = ["username", "email", "password","url","groups"]

