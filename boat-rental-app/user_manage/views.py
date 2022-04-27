from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EditUserForm_Email, EditUserForm_fname, EditUserForm_lname, EditUserForm_phone
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile_view_form(request, form_url=None):
    if request.method == 'POST':
        # pass string through URL
        if form_url == 'email':
            form = EditUserForm_Email(request.POST, instance=request.user)
        elif form_url == 'fname':
            form = EditUserForm_fname(request.POST, instance=request.user)
        elif form_url == 'lname':
            form = EditUserForm_lname(request.POST, instance=request.user)
        elif form_url == 'phone':
            form = EditUserForm_phone(request.POST, instance=request.user)
        else:
            return render(request, 'profile.html')

        if form.is_valid():
            form.save()
            return redirect('profile', form_url='None')
    else:
        email_form = EditUserForm_Email()
        fname_form = EditUserForm_fname()
        lname_form = EditUserForm_lname()
        phone_form = EditUserForm_phone()
            
    context = {
        'email_form' : email_form,
        'fname_form' : fname_form,
        'lname_form' : lname_form,
        'phone_form' : phone_form
    }
    return render(request, 'profile.html', context)


