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


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
