""" This module contains the URL pattern for the Contact app. """

from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
]