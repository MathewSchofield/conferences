from django import forms

class NewForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
