""" This module contains the form logic for creating a message. """

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    """ 
    Users can use the form to send a message by filling in the fields listed below.
    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')