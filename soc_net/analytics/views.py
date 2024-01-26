from datetime import date

from django.db.models import Count
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework import generics, permissions

from soc_net.posts.models import Like
from soc_net.users.models import Profile

from .permissions import IsSuperUser
from .serializers import LikeAnalyticsSerializer, UserAnalyticsSerializer
from .utils import get_formatted_dates


class UserAnalyticsView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserAnalyticsSerializer
    permission_classes = (permissions.IsAdminUser, IsSuperUser)


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                name="date_from",
                description="Filter start date",
                type=date,
                examples=[
                    OpenApiExample(
                        name="2020-02-02",
                        value="2020-02-02",
                        summary="Example date_from: 2020-02-02",
                    ),
                    OpenApiExample(
                        name="2024-01-20",
                        value="2024-01-20",
                        summary="Example date_from: 2024-01-20",
                    ),
                ],
            ),
            OpenApiParameter(
                name="date_to",
                description="Filter end date",
                type=date,
                examples=[
                    OpenApiExample(
                        name="2020-02-15",
                        value="2020-02-15",
                        summary="Example date_to: 2020-02-15",
                    ),
                    OpenApiExample(
                        name="2024-04-20",
                        value="2024-04-20",
                        summary="Example date_to: 2024-04-20",
                    ),
                ],
            ),
        ],
    )
)
class LikeAnalyticsView(generics.ListAPIView):
    serializer_class = LikeAnalyticsSerializer
    permission_classes = (permissions.IsAdminUser, IsSuperUser)

    def get_queryset(self, *args, **kwargs):
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")

        date_from_midnight, date_to_midnight = get_formatted_dates(date_from, date_to)

        return (
            Like.objects.filter(
                created_at__range=(date_from_midnight, date_to_midnight)
            )
            .values("created_at__date")
            .annotate(like_count=Count("id"))
        )
