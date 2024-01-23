from rest_framework import generics, permissions

from .models import Post
from .serializers import CreatePostSerializer


class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = (permissions.IsAuthenticated,)
