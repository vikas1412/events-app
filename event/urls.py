from django.urls import path
from event import views

from event.views import EventsListView

urlpatterns = [
    path('', views.index, name="index"),
    

    path('places/', views.PlacesListView.as_view(), name="places"),
]