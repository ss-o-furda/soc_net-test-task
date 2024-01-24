from django.urls import path

from .views import CreateLikeView, CreatePostView

urlpatterns = [
    path("", CreatePostView.as_view(), name="create_post"),
    path(
        "<int:pk>/like",
        CreateLikeView.as_view(),
        name="like__post",
    ),
]
