from django.utils import timezone

from .models import Profile


class LastRequestMiddleware:
    """
    Middleware to update the last_request field for each user on each request.

    This middleware updates the last_request field in the Profile
    instance to reflect the timestamp of the user's last request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            Profile.objects.filter(user=request.user).update(
                last_request=timezone.now()
            )

        return response
