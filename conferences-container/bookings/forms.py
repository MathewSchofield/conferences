from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["title", "first_name", "last_name", "email"]


class BookingForm2(ModelForm):
    class Meta:
        model = Booking
        fields=["home_church"]
