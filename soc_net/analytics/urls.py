from django.urls import path

from .views import LikeAnalyticsView, UserAnalyticsView

urlpatterns = [
    path("users", UserAnalyticsView.as_view(), name="users_analytics"),
    path("likes", LikeAnalyticsView.as_view(), name="likes_analytics"),
]
