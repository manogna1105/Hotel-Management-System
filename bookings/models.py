# bookings/models.py
from django.db import models
from users.models import CustomUser  # update if in another app
from rooms.models import Room

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    special_requests = models.TextField(blank=True, null=True)

    payment_method = models.CharField(max_length=50)
    card_number = models.CharField(max_length=20)
    card_name = models.CharField(max_length=100)
    expiry = models.CharField(max_length=10)
    cvv = models.CharField(max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.room.name} on {self.created_at.strftime('%Y-%m-%d')}"

    
class RoomAvailability(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='availability')
    total_rooms = models.PositiveIntegerField()
    available_rooms = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.room.name} - Available: {self.available_rooms}/{self.total_rooms}"

