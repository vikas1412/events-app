from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from event.filters import EventFilter
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

    def get_context_data(self, **kwargs):
        context = super(EventsDetailView, self).get_context_data(**kwargs)
        return context


class NewEventCreateView(LoginRequiredMixin, generic.CreateView):
    model = Event
    template_name = 'events/new-event.html'
    fields = ['title', 'place', 'type_of_place', 'date', 'tags', 'description', 'time_start', 'time_end']
    context_object_name = 'new_event'

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        year, month, day = str(form.instance.date).split('-')
        print(year, '\n', month, '\n', day)

        form.instance.year = int(year)
        form.instance.month = int(month)
        form.instance.day = int(day)
        form.instance.all_day = True
        return super(NewEventCreateView, self).form_valid(form)


class NewPlaceCreateView(LoginRequiredMixin, generic.CreateView):
    model = PlaceType
    template_name = 'events/new-place.html'
    fields = ['place_type']
    context_object_name = 'new_place'
    success_url = '/events/places/'


class NewPlaceDetailCreateView(LoginRequiredMixin, generic.CreateView):
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


def filter_events(request):

    events = Event.objects.all()
    print(events)
    event_filter = EventFilter(request.GET, queryset=events)
    events = event_filter.qs

    params = {
        'filter': event_filter,
        'events': events,
    }
    return render(request, 'events/filter.html', params)