from django.db import models
from django.utils import timezone

class Booking(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    slots = models.PositiveIntegerField(default=15)

    def __str__(self):
        return f"Booking for {self.date} with {self.slots} slots left"


