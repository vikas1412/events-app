from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from event.forms import SignUpForm
from event.models import Event, Place, PlaceType


def index(request):
    return render(request, 'events/index.html')


class PlacesListView(generic.ListView):
    model = Place
    template_name = 'events/places.html'
    context_object_name = 'places'
