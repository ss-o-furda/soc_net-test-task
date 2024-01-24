"""
info about using serializers for rest_framework_simplejwt.views:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/drf_yasg_integration.html
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, validators

from .models import Profile
from .utils import get_tokens_for_user


class TokenObtainPairSuccessResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenObtainPairFailedResponseSerializer(serializers.Serializer):
    details = serializers.CharField(
        default="No active account found with the given credentials"
    )

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshSuccessResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshFailedResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Token is invalid or expired")
    code = serializers.CharField(default="token_not_valid")

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(
        required=True, validators=[validators.UniqueValidator(User.objects.all())]
    )
    username = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "access", "refresh", "password")

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        tokens = get_tokens_for_user(user)

        Profile.objects.create(user=user)

        return {
            "id": user,
            "email": user.email,
            "username": user.username,
            "access": tokens["access"],
            "refresh": tokens["refresh"],
        }
