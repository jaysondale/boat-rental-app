from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from django import forms

class event_form(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'startTime', 'endTime', 'Interested', 'category']