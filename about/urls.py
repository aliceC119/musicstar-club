""" This module contains the URL pattern for the about app. """

from . import views
from django.urls import path

urlpatterns = [
    path('about', views.about_me, name='about'),
]