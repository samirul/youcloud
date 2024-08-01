from rest_framework import serializers, exceptions
from accounts.models import User
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate



class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

