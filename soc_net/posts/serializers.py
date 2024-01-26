from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import exceptions, serializers

from soc_net.users.serializers import RegisterSerializer

from .models import Like, Post


class CreatePostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes_count = serializers.IntegerField(read_only=True)
    author_data = RegisterSerializer(read_only=True, source="author")

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("author_data",)


class LikePostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_data = RegisterSerializer(read_only=True, source="user")
    post = CreatePostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ("user_data",)

    def create(self, validated_data):
        post_id = self.context.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        validated_data["post"] = post
        try:
            instance = super().create(validated_data)
        except IntegrityError:
            raise exceptions.ValidationError({"error": "User already liked this post!"})
        return instance
