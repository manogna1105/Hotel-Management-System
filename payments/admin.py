from django.contrib import admin
from .models import BookingInfo, BookedRoom
# Register your models here.
admin.site.register(BookingInfo)
admin.site.register(BookedRoom)