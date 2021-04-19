from django.shortcuts import render
from .forms import CustomUserCreationForm

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