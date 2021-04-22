from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from .models import Boat, Booking
from django import forms
from phonenumber_field.formfields import PhoneNumberField


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

class TempNewUserForm(Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    phone_number = PhoneNumberField(region="CA")
    email = forms.EmailField() 


class StaffRentalBookingForm(ModelForm):
    def __init__(self, users, rentalItems, *args, **kwargs):
        super(StaffRentalBookingForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search':"true"}), choices=users)
        self.fields['rentalItem'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search':"true"}), choices=rentalItems)
    
    class Meta:
        model = Booking
        fields = ['startDay', 'endDay']
        widgets = {
            'startDay': DateInput(attrs={'class': 'form-control'}),
            'endDay' : DateInput(attrs={'class': 'form-control mt-2'})
        }