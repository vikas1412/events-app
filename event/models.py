from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class PlaceType(models.Model):
    place_type = models.CharField(max_length=200, help_text="Enter place type")

    def __str__(self):
        return self.place_type


class Place(models.Model):
    title = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)
    tags = TaggableManager(blank=True)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    type_of_place = models.ForeignKey('PlaceType', on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', args=[str(self.id)])

    @property
    def lat_lon(self):
        return list(getattr(self.location, 'coords', [])[::-1])


class Event(models.Model):
    title = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, null=True)

    year = models.IntegerField(blank=True, default=None, null=True)
    month = models.IntegerField(blank=True, default=None, null=True)
    day = models.IntegerField(blank=True, default=None, null=True)

    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    type_of_place = models.ForeignKey('PlaceType', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    all_day = models.BooleanField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('event', args=[str(self.id)])

    def __str__(self):
        return self.title

    @property
    def lat_lon(self):
        return list(getattr(self.place, 'coords', [])[::-1])