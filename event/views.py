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


class NewEventCreateView(generic.CreateView):
    model = Event
    template_name = 'events/new-event.html'
    fields = ['title', 'place', 'type_of_place', 'tags', 'description', 'time_start', 'time_end']
    context_object_name = 'new_event'


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
            else:
                return HttpResponse("Invalid username & password")

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})