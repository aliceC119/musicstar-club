""" This module contains the admin logic for the About app. """

from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin
from .models import Location
from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField


# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    """
    Allows admins to create the content of the about page.
    """

    summernote_fields = ('content',)


class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {'widget': GoogleMapsAddressWidget},
    }


admin.site.register(Location, LocationAdmin)