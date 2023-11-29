from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        #fields = ["title", "first_name", "last_name", "email", "home_church", "completed"]
        fields = ["first_name"]





#from django import forms
#class NewForm(forms.Form):
#    first_name = forms.CharField(label="First name", max_length=100)
