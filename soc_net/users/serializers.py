# info: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/drf_yasg_integration.html
from rest_framework import serializers


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
