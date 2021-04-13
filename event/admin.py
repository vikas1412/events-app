from django.contrib import admin

from event.models import Event, PlaceType

admin.site.register('PlaceType',)


@admin.register(Event)
class EventsInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'created_by')
