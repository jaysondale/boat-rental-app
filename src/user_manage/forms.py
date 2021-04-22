from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

class EditUserForm_Email(ModelForm):
    class Meta:
        model = User
        fields = ['email']

class EditUserForm_fname(ModelForm):
    class Meta:
        model = User
        fields = ['first_name']

class EditUserForm_lname(ModelForm):
    class Meta:
        model = User
        fields = ['last_name']

class EditUserForm_phone(ModelForm):
    class Meta:
        model = User
        fields = ['phone']


