from django.contrib.auth.models import User
from rest_framework import serializers

from soc_net.users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "last_login")


class UserAnalyticsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=UserSerializer())
    id = serializers.IntegerField(source="user.id")
    username = serializers.CharField(source="user.username")
    last_login = serializers.DateTimeField(source="user.last_login")

    class Meta:
        model = Profile
        fields = ("user", "id", "username", "last_login", "last_request")


class LikeAnalyticsSerializer(serializers.Serializer):
    date = serializers.DateField(source="created_at__date")
    like_count = serializers.IntegerField()
