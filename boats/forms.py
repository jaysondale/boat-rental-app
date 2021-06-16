from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from .models import Boat, Booking
from django import forms
from phonenumber_field.formfields import PhoneNumberField
import json


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
            'startDay': DateInput(attrs={'class': 'form-control datechk'}),
            'endDay' : DateInput(attrs={'class': 'form-control mt-2 datechk'})
        }

class SpecialModelChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        super(SpecialModelChoiceField, self).__init__(*args, **kwargs)
        self.prices = {}
        for obj in self._get_queryset():
            self.prices[f'{obj.name}'] = {'dayPrice': str(obj.dayPrice), 'weekPrice': str(obj.weekPrice)}

    def get_prices(self):
        return json.dumps(self.prices)

class RentalConfirmForm(Form):
    def __init__(self, *args, **kwargs):
        super(RentalConfirmForm, self).__init__(*args, **kwargs)
        self.rqs = Boat.objects.all()
        self.fields['rentalItem'] = SpecialModelChoiceField(self.rqs, widget=forms.Select(attrs={'id': 'booking-rental-item','class': 'selectpicker', 'data-live-search':"true"}))
    startDay = forms.DateField(widget=DateInput(attrs={'id': 'booking-start-day', 'class': 'form-control'}))
    endDay = forms.DateField(widget=DateInput(attrs={'id': 'booking-end-day', 'class': 'form-control'}))
    price = forms.DecimalField(max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={'id': 'booking-price', 'class': 'form-control'}))

class TempNewUserForm(Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'new-user-field'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class':'new-user-field'}))
    phone_number = PhoneNumberField(region="CA", widget=forms.TextInput(attrs={'class':'new-user-field'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'new-user-field'}))


class StaffRentalBookingForm(ModelForm):
    def __init__(self, *args, uqs, rqs, **kwargs):
        super(StaffRentalBookingForm, self).__init__(*args, **kwargs)
        self.uqs = uqs
        self.rqs = rqs
        self.fields['user'] = forms.ModelChoiceField(self.uqs, widget=forms.Select(attrs={'class': 'selectpicker existing-user-field', 'data-live-search':"true"}), required=False)
        self.fields['rentalItem'] = forms.ModelChoiceField(self.rqs, widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search':"true"}))
    
    class Meta:
        model = Booking
        fields = ['startDay', 'endDay', 'user', 'rentalItem', 'price']
        widgets = {
            'startDay': DateInput(attrs={'class': 'form-control'}),
            'endDay' : DateInput(attrs={'class': 'form-control mt-2'})
        }