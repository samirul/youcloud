import requests
from rest_framework import serializers
from django.core.files.base import ContentFile
from accounts.models import User
from rest_framework.authtoken.models import Token
from allauth.socialaccount.models import SocialAccount


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user
    

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]