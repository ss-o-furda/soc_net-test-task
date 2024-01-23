"""
info about using rest_framework_simplejwt.views:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/drf_yasg_integration.html
"""
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import (
    RegisterSerializer,
    TokenObtainPairFailedResponseSerializer,
    TokenObtainPairSuccessResponseSerializer,
    TokenRefreshFailedResponseSerializer,
    TokenRefreshSuccessResponseSerializer,
)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @extend_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: TokenObtainPairFailedResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @extend_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: TokenRefreshFailedResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
