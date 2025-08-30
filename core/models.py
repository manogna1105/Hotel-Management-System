from django.db import models
from bookings.models import Booking

# Create your models here.
class IndividualService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    icon = models.CharField(max_length=50, blank=True)  # Optional for UI

    def __str__(self):
        return f"{self.name} (${self.price})"

class ServicePackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    features = models.ManyToManyField(IndividualService, blank=True)
    color = models.CharField(max_length=20, default='blue')

    def __str__(self):
        return f"{self.name} Package (${self.price})"

class BookingService(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='package_services')
    package = models.ForeignKey(ServicePackage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.package.name} for booking {self.booking.id}"

class BookingIndividualService(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='individual_services')
    service = models.ForeignKey(IndividualService, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.service.name} for booking {self.booking.id}"


