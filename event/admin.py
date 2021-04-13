from django.contrib import admin

from event.models import Event


@admin.register(Event)
class EventsInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'place_location', 'updated_at', 'created_by')
