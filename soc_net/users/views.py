# info: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/drf_yasg_integration.html
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import (
    TokenObtainPairFailedResponseSerializer,
    TokenObtainPairSuccessResponseSerializer,
    TokenRefreshFailedResponseSerializer,
    TokenRefreshSuccessResponseSerializer,
)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: TokenObtainPairFailedResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: TokenRefreshFailedResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
