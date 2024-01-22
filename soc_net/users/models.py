from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(
        User, verbose_name=_("django user"), on_delete=models.CASCADE
    )
    last_request = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"user: {self.user.username} | last_request: {self.last_request.strftime('%a %d %b %Y, %I:%M%p')}"
