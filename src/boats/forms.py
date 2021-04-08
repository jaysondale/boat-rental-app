from django.forms import ModelForm
from .models import Boat
from django import forms

class rental_form(ModelForm):
    class Meta:
        model = Boat
        fields = ['name', 'description', 'dayPrice', 'weekPrice', 'hp', 'capacity']

class DateInput(forms.DateInput):
    input_type = 'date'

class DateInput_form(ModelForm):

    class Meta:
        model = Boat
        fields = ['startDay', 'endDay']
        widgets = {
            'startDay': DateInput(attrs={'class': 'form-control'}),
            'endDay' : DateInput(attrs={'class': 'form-control mt-2'})
        }