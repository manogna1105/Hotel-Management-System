from django.contrib import admin

# Register your models here.
from .models import ServicePackage, IndividualService, BookingService, BookingIndividualService

admin.site.register(IndividualService)
admin.site.register(ServicePackage)
admin.site.register(BookingService)
admin.site.register(BookingIndividualService)