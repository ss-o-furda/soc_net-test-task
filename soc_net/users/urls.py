from django.urls import path

from .views import DecoratedTokenObtainPairView, DecoratedTokenRefreshView, RegisterView

urlpatterns = [
    path("/login", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("/refresh-token", DecoratedTokenRefreshView.as_view(), name="token_refresh"),
    path("/register", RegisterView.as_view(), name="register new user"),
]
