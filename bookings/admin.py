from django.contrib import admin
from .models import Booking,RoomAvailability

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'user__username')
    list_filter = ('created_at', 'country', 'payment_method')

admin.site.register(RoomAvailability)