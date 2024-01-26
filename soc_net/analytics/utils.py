from datetime import datetime, time

from django.utils.timezone import make_aware
from rest_framework import exceptions


def _validate_dates(_date_from, _date_to):
    if _date_from > _date_to:
        raise exceptions.ValidationError(
            {"error": "The start date cannot be later than the end date!"}
        )
    if _date_to < _date_from:
        raise exceptions.ValidationError(
            {"error": "The end date cannot be earlier than the start date!"}
        )


def get_formatted_dates(_date_from, _date_to):
    try:
        date_from = datetime.strptime(_date_from, "%Y-%m-%d").date()
        date_to = datetime.strptime(_date_to, "%Y-%m-%d").date()
    except ValueError:
        raise exceptions.ValidationError({"error": "Invalid date format"})

    _validate_dates(date_from, date_to)

    date_from_midnight = make_aware(datetime.combine(date_from, time.min))
    date_to_midnight = make_aware(datetime.combine(date_to, time.max))

    return date_from_midnight, date_to_midnight
