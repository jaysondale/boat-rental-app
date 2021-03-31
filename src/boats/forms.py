from django.forms import ModelForm
from .models import Boat

class rental_form(ModelForm):
    class Meta:
        model = Boat
        fields = ['name', 'description', 'dayPrice', 'weekPrice', 'hp', 'capacity']

