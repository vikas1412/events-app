from django.contrib.auth.models import User
from django.contrib.gis.db import models
# from django.db import models
from taggit.managers import TaggableManager


class PlaceType(models.Model):
    place_type = models.CharField(max_length=200, help_text="Enter place type")

    def __str__(self):
        return self.place_type


class Event(models.Model):
    title = models.CharField(max_length=200)
    place_location = models.PointField(blank=True, null=True)
    tags = TaggableManager()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    type_of_place = models.ForeignKey('PlaceType', on_delete=models.SET_NULL, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def lat_lon(self):
        return list(getattr(self.location, 'coords', [])[::-1])
