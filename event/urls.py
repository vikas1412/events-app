from django.urls import path
from event import views

from event.views import EventsListView

urlpatterns = [
    path('', views.index, name="index"),

    path('all/', EventsListView.as_view(), name="events"),

    path('add/place-type/', views.NewPlaceCreateView.as_view(), name="new-place"),

    path('add/place/', views.NewPlaceDetailCreateView.as_view(), name="new-place-detail"),


    path('places/', views.PlacesListView.as_view(), name="places"),
]