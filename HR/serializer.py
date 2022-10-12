from rest_framework import serializers
from .models import ProfileModel
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # la methode create() est utilisée car le password doit être hasché
    def create(self, validated_data):
        print("Aziz validated_data",validated_data)
        user = User.objects.create_user(username=validated_data["username"],password=validated_data["password"])
        user.save()
        return user


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password')
    class Meta:
        model = ProfileModel
        fields = ["username", "email", "password","url"]
