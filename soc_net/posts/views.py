from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Like, Post
from .serializers import CreatePostSerializer, LikePostSerializer


class CreatePostView(generics.CreateAPIView):
    serializer_class = CreatePostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateLikeView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        post_id = kwargs.get("pk", None)
        post = get_object_or_404(Post, pk=post_id)

        like_data = {"user": request.user.id, "post": post_id}

        like_exists = Like.objects.filter(**like_data).exists()
        if like_exists:
            return Response(
                {"error": "User already liked the post"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        like_serializer = self.get_serializer(data=like_data)
        like_serializer.is_valid(raise_exception=True)
        like_serializer.save()

        post.likes_count = F("likes_count") + 1
        post.save()

        headers = self.get_success_headers(like_serializer.data)
        return Response(
            like_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        post_id = kwargs.get("pk", None)
        post = get_object_or_404(Post, pk=post_id)
        try:
            like = Like.objects.get(post=post, user=request.user)
        except Like.DoesNotExist:
            return Response(
                {"error": "User has not liked the post"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if post.likes_count > 0:
            post.likes_count = F("likes_count") - 1
            post.save()

        self.perform_destroy(like)
        return Response(status=status.HTTP_204_NO_CONTENT)
