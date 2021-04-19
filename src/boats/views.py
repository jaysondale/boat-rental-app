from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from datetime import date, timedelta
from django.http import HttpResponse
from .models import Boat, Booking
from .forms import rental_form, BoatBookingForm, UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Value

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

@staff_member_required
def upcoming_rentals_view(request, new_date=None):
	today = date.today()
	curr_date = today if (new_date == None) else new_date
	prev_date = curr_date - timedelta(days=1)
	next_date = curr_date + timedelta(days=1)

	today_out = Booking.objects.filter(startDay=curr_date)
	today_return = Booking.objects.filter(endDay=curr_date)

	context = {
		'today': today,
		'today_out': today_out,
		'today_return': today_return,
		'prev_date':  prev_date,
		'curr_date': curr_date,
		'next_date': next_date,
		'prev_is_today': prev_date == today,
		'curr_is_today': curr_date == today,
		'next_is_today': next_date == today
	}
	return render(request, 'boats/upcoming_rentals.html', context)

@staff_member_required
def rental_requests_view(request):
	context = {

	}
	return render(request, 'boats/rental_requests.html', context)

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
		form = rental_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('boat_post_form')
	else:
		print('not valid')
		form = rental_form()
	context = {
		'form' : form
	}
	return render(request, 'boats/boat_post_form.html', context)


def delete_booking(request, booking_id=None):
	booking = Booking.objects.get(id=booking_id)
	booking.delete()
	bookings = Booking.objects.filter(user=request.user)
	return redirect("bookings")
	
