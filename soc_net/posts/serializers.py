from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from .models import Like, Post


class CreatePostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        return Post.objects.create(
            author=validated_data["author"],
            title=validated_data["title"],
            content=validated_data["content"],
        )


@extend_schema_serializer(
    exclude_fields=("user", "post"),
    examples=[
        OpenApiExample(
            "Correct response",
            value={
                "id": 0,
                "user": 0,
                "post": 0,
                "created_at": "2024-01-24T22:33:20.202Z",
            },
            response_only=True,
        ),
    ],
)
class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
