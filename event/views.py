from django.shortcuts import render
from django.views import generic

from event.models import Event


def index(request):
    return render(request, 'events/index.html')


class EventsListView(generic.ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'