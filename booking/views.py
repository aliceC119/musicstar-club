from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.decorators import login_required



def get_first_saturday():
    today = now().date()
    first_saturday = today + timedelta((5 - today.weekday()) % 7)
    return first_saturday

@login_required
def booking_view(request):
    first_saturday = get_first_saturday()
    booking, created = Booking.objects.get_or_create(date=first_saturday)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid() and booking.slots > 0:
            booking.slots -= 1
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'booking/booking_form.html', {'form': form, 'slots': booking.slots})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

def book_slots(request):
    available_slots = Booking.slots_available()
    if available_slots <= 0:
        return render(request, 'no_seats_available.html')