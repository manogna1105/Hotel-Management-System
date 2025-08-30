from django.conf import settings
from django.db import models
from rooms.models import Room
from core.models import IndividualService, ServicePackage

class BookingInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)  # <-- Add this line
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    services = models.TextField(blank=True)  # store comma-separated IDs
    packages = models.TextField(blank=True)  # store comma-separated IDs

    def __str__(self):
        return f"{self.user.username} - {self.room.name} - ₹{self.total_cost}"


class BookedRoom(models.Model):
    booking_info = models.ForeignKey(
        BookingInfo,
        on_delete=models.CASCADE,
        related_name='booked_rooms',
        null=True,  # Allow existing rows to have NULL temporarily
        blank=True
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

