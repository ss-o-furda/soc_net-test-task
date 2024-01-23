from rest_framework import serializers

from .models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ("id", "author", "title", "content")

    def create(self, validated_data):
        return Post.objects.create(
            author=validated_data["author"],
            title=validated_data["title"],
            content=validated_data["content"],
        )
