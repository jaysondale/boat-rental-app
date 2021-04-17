from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import Boat, Booking, Event
from .forms import rental_form, BoatBookingForm, UserCreationForm

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
	context = {

	}
	return render(request, 'boats/marine.html', context)

def contact_view(request):
	context = {

	}
	return render(request, 'boats/contact.html', context)

def bookings_view(request):
	isAuthenticated = True
	if (request.user.is_authenticated):
		bookings = Booking.objects.filter(user=request.user)
	else:
		bookings = None
		isAuthenticated = False
	context = {
		"bookings": bookings,
		"noBookings": bookings.count() == 0 if bookings != None else True,
		"isAuthenticated": isAuthenticated
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
	form = BoatBookingForm()
	# insert logic to save the date range 
	context = {
		'boats': boats,
		'form' : form
	}
	return render(request, 'boats/water.html', context)

def book_boat(request, boat_id=None):
	if request.method == 'POST':
		form = BoatBookingForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.rentalItem = Boat.objects.get(id=boat_id)
			obj.user = request.user
			obj.save()
			return redirect('bookings')
	else:
		print("Error booking boat")
	redirect('water_activities')


def boat_form_view(request):
	if request.method == 'POST':
		form = rental_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('boat_post_form')
	else:
		form = rental_form()
	context = {
		'form' : form
	}
	return render(request, 'boats/boat_post_form.html', context)


def delete_booking(request, booking_id=None):
	booking = Booking.objects.get(id=booking_id)
	booking.delete()
	bookings = Booking.objects.filter(user=request.user)
	redirect("bookings")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'boats/signup.html', {'form': form})

def events_view(request, event_id=None):
	events = Event.objects.all()
	if event_id == 'Arts':
		events = Event.objects.filter(category='Arts')
	elif event_id == 'Sports':
		events = Event.objects.filter(category='Sports')
	elif event_id == 'Food':
		events = Event.objects.filter(category='Food')
	# when results are not filtered
	else:
		events = Event.objects.all()

	context = {
		'events': events
	}
	return render(request, 'boats/events.html', context)

