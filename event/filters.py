from event.models import *
import django_filters


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['year', 'month', 'day', 'date']
