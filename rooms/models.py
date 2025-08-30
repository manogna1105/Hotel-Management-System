from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('deluxe', 'Deluxe Room'),
        ('executive', 'Executive Room'),
        ('premium', 'Premium Suite'),
        ('family', 'Family Suite'),
        ('penthouse', 'Penthouse Suite'),
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    guest_capacity = models.IntegerField()
    bed_count = models.IntegerField()
    size = models.IntegerField(help_text="Size in square meters")
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/')
    rating = models.FloatField()
    reviews_count = models.IntegerField()

    # Amenities as boolean fields (you can normalize if needed)
    wifi = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    jacuzzi = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    minibar = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)

    def __str__(self):
        return self.name
