from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Boat
from .forms import rental_form


# Create your views here.
def boat_detail_view(request):
	boats = Boat.objects.all()

	context = {
		'page_title': 'KLM Boat Rentals',
		'boats': boats,
	}

	return render(request, "boats/main.html", context)

# ModelForm passed to form page 
def item_rental_form(request):
	if request.method == 'POST':
		form = rental_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('item_rental_form')
	else:
		form = rental_form()
	context = {
		'form' : form
	}
	return render(request, 'boats/form.html', context)


