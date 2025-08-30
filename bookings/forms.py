from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'room', 'check_in', 'check_out',
            'first_name', 'last_name', 'email', 'phone',
            'address', 'city', 'country', 'special_requests',
            'card_number', 'card_name', 'expiry', 'cvv', 'payment_method'
        ]
    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if room and check_in and check_out:
            conflicts = Booking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            )
            if conflicts.exists():
                raise ValidationError("This room is not available for the selected dates.")
        return cleaned_data
