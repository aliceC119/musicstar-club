""" This module contains the admin logic for the Contact app. """

from django.contrib import admin
from .models import Contact, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Contact)
class AboutAdmin(SummernoteModelAdmin):

    """ 
    Admin can view the sent messages.
    """
    summernote_fields = ('content',)
    list_display = ('message',)