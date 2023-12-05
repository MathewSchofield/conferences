from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["title", "first_name", "last_name", "email"]
        widgets = {
            # 'title': MultipleHiddenInput(attrs={
            #     'class': 'form-control',
            #     'style': 'max-width: 50px;',
            # }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'First Name',
                'required': True
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name',
                'required': True
            }),
            'email': EmailInput(attrs={
                'class': 'form-control', 
                'style': 'max-width: 300px;',
                'placeholder': 'Email',
                'required': True
                })
        }


class BookingForm2(ModelForm):
    class Meta:
        model = Booking
        fields=["home_church"]
        widgets = {
            'home_church': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Home Church',
                'required': True
            }),
        }
