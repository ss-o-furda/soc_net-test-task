from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """
    FOR DISCUSSION: leave property with count or create additional field and
    update Like create view to update this field each time user likes post
    leave property:
        pros:
            1. speed up development
        cons:
            1. additional DB request for each post view
    change to field:
        pros:
            1. no additional request to show likes count
        cons:
            1. harder to keep sync
            2. will slightly slow down the development

    In general, as long as the project is used by three users, two of whom are developers,
    it's not a bad idea to leave the property.
    """

    @property
    def likes_count(self):
        return self.like_set.count()

    def __str__(self):
        return f"{self.title} | author: {self.author.username}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["post", "user"]

    def __str__(self):
        return f"post: {self.post.title} | user: {self.user.username}"
