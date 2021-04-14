from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from event.forms import SignUpForm
from event.models import Event, Place, PlaceType


def index(request):
    return render(request, 'events/index.html')


class EventsListView(generic.ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'


class EventsDetailView(generic.DetailView):
    model = Event
    template_name = 'events/event.html'
    context_object_name = 'event'


class NewPlaceCreateView(generic.CreateView):
    model = PlaceType
    template_name = 'events/new-place.html'
    fields = ['place_type']
    context_object_name = 'new_place'
    success_url = '/events/places/'


class NewPlaceDetailCreateView(generic.CreateView):
    model = Place
    template_name = 'events/new-place-detail.html'
    fields = ['title', 'type_of_place', 'tags', 'location', 'description', 'address', 'phone', 'city']
    context_object_name = 'new_place'
    success_url = '/events/places/'


class PlacesListView(generic.ListView):
    model = Place
    template_name = 'events/places.html'
    context_object_name = 'places'

