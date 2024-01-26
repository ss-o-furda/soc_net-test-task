from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from .models import Like
from .serializers import CreatePostSerializer, LikePostSerializer


class CreatePostView(generics.CreateAPIView):
    serializer_class = CreatePostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateLikeView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"post_id": self.kwargs.get("pk")})
        return context

    def get_object(self):
        return get_object_or_404(
            Like, user=self.request.user, post__id=self.kwargs.get("pk")
        )
