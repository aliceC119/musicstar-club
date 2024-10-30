""" This module contains a model for the Contact app. """

from django.db import models

# Create your models here.
class Contact(models.Model):

    """ 
    It is to set the fields that are required in a contact form
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact request from {self.name}"
