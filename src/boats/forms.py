from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Boat, Booking
from django import forms

class rental_form(ModelForm):
    class Meta:
        model = Boat
        fields = ['name', 'description', 'image', 'dayPrice', 'weekPrice', 'hp', 'capacity']

class DateInput(forms.DateInput):
    input_type = 'date'

class BoatBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['startDay', 'endDay']
        widgets = {
            'startDay': DateInput(attrs={'class': 'form-control'}),
            'endDay' : DateInput(attrs={'class': 'form-control mt-2'})
        }