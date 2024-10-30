""" This module contains the models for the About app. """


from django.db import models
from cloudinary.models import CloudinaryField
from django_google_maps import fields as map_fields


# Create your models here.

class About(models.Model):

    """
    The Model of the about app.

    It is to set the essential fields for the admin to write the about page.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return self.title

    """
    This Model is for putting the location from google maps.
    """


class Location(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)