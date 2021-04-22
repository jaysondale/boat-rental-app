from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EditUserForm
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

def profile_view(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        print ('not valid')
        form = EditUserForm()
    context = {
        'form' : form
    }
    return render(request, 'profile.html', context)



