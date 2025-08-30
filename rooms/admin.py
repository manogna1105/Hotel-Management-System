from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'price', 'guest_capacity', 'bed_count', 'rating')
    list_filter = ('room_type', 'guest_capacity', 'wifi', 'breakfast', 'jacuzzi')
    search_fields = ('name', 'description')