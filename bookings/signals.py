# bookings/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Booking, RoomAvailability

@receiver(post_save, sender=Booking)
def reduce_availability(sender, instance, created, **kwargs):
    if created:
        try:
            availability = instance.room.availability
            if availability.available_rooms > 0:
                availability.available_rooms -= 1
                availability.save()
            else:
                # Optional: log error or prevent booking elsewhere
                pass
        except RoomAvailability.DoesNotExist:
            pass

@receiver(post_delete, sender=Booking)
def increase_availability(sender, instance, **kwargs):
    try:
        availability = instance.room.availability
        if availability.available_rooms < availability.total_rooms:
            availability.available_rooms += 1
            availability.save()
    except RoomAvailability.DoesNotExist:
        pass
