from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from event.models import Event, PlaceType, Place

admin.site.register(PlaceType)


@admin.register(Event)
class EventsInstanceAdmin(OSMGeoAdmin):
    default_lon = 30.287842565701155
    default_lat = 78.10559462066462
    default_zoom = 12
    list_display = ('title', 'updated_at', 'created_by')


@admin.register(Place)
class PlaceInstanceAdmin(OSMGeoAdmin):
    default_lon = 30.287842565701155
    default_lat = 78.10559462066462
    default_zoom = 12
    list_display = ('title', 'city', 'type_of_place', 'timestamp')
