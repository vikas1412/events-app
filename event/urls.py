from django.urls import path
from event import views

from event.views import EventsListView


urlpatterns = [
    path('', views.index, name="index"),

    path('all/', EventsListView.as_view(), name="events"),
]