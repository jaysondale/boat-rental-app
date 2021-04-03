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

# has an example of a model form 
def marine_view(request):
	if request.method == 'POST':
		form = rental_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('marine_view')
	else:
		form = rental_form()
	context = {
		'form' : form
	}
	return render(request, 'boats/marine.html', context)

def events_view(request):
	context = {

	}
	return render(request, 'boats/events.html', context)

def contact_view(request):
	context = {

	}
	return render(request, 'boats/contact.html', context)

def bookings_view(request):
	context = {

	}
	return render(request, 'boats/bookings.html', context)

def activities_view(request):
	context = {

	}
	return render(request, 'boats/activities.html', context)

def land_activities_view(request):
	boats = Boat.objects.all()
	context = {
		'boats': boats
	}
	return render(request, 'boats/land.html', context)

def water_activities_view(request):
	boats = Boat.objects.all()
	context = {
		'boats': boats
	}
	return render(request, 'boats/water.html', context)




