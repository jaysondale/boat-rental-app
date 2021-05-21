from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from datetime import date, timedelta, datetime
#from dateutil.relativedelta import *
from django.http import HttpResponse, JsonResponse
from .models import Boat, Booking, RentalItem
from .forms import rental_form, BoatBookingForm, UserCreationForm, StaffRentalBookingForm, TempNewUserForm, RentalConfirmForm
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.db.models import Count, F, Value
from django.utils.safestring import mark_safe
import calendar
from .utils import Calendar
from django.contrib.auth import get_user_model
from django.urls import reverse


def bookings_view(request):
	isAuthenticated = True
	if (request.user.is_authenticated):
		bookings = Booking.objects.filter(user=request.user)
	else:
		bookings = None
		isAuthenticated = False
	context = {
		"page_title": 'My Bookings',
		"bookings": bookings,
		"noBookings": bookings.count() == 0 if bookings != None else True,
		"isAuthenticated": isAuthenticated
	}
	return render(request, 'boats/bookings.html', context)

def land_activities_view(request):
	boats = Boat.objects.all()
	context = {
		'boats': boats
	}
	return render(request, 'boats/land.html', context)

def rentals_view(request, next=None):
	boats = Boat.objects.all()
	form = BoatBookingForm()
	# insert logic to save the date range 
	context = {
		"page_title": 'Rentals',
		'boats': boats,
		'form' : form
	}
	return render(request, 'boats/water.html', context)

def book_boat(request, boat_id=None):
	if request.method == 'POST':
		if (request.user.is_authenticated):
			form = BoatBookingForm(request.POST)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.rentalItem = Boat.objects.get(id=boat_id)
				obj.user = request.user
				obj.price = Booking.DEFAULT_PRICE
				obj.save()
				return redirect('bookings')
		else:
			return redirect('/accounts/login/?next=/rentals/')
		
	else:
		print("Error booking boat")
	return redirect('water_activities')

def user_delete_booking(request, booking_id=None):
	booking = Booking.objects.get(id=booking_id)
	usr = request.user
	if usr.is_authenticated:
		if usr == booking.user:
			booking.delete()
			bookings = Booking.objects.filter(user=request.user)
	return redirect("bookings")

# RENTAL MANAGEMENT -> STAFF ONLY VIEWS
# Show upcoming rentals
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

# Rental booking management views

@staff_member_required
def staff_delete_booking(request, booking_id=None):
	booking = Booking.objects.get(id=booking_id)
	booking.delete()
	return redirect('calendar')

@staff_member_required
def staff_delete_booking_ajax(request):
	if (request.method == 'POST'):
		booking = Booking.objects.get(id=request.POST['bid'])
		print(booking)
		booking.delete()
		return JsonResponse({'code': 200})
	return JsonResponse({'code': 400})

@staff_member_required
def get_booking_data(request, booking_id=None):
	if booking_id != None:
		booking = Booking.objects.get(id=booking_id)
		user = booking.user
		return JsonResponse({'name': user.get_full_name(),
			'email': user.email,
			'rentalItem': booking.rentalItem.name,
			'startDay': booking.startDay,
			'endDay': booking.endDay,
			'price': booking.price,
			'save_url': reverse("confirm_booking", kwargs={'booking_id': booking.pk})
			})

@staff_member_required
def confirm_booking(request, booking_id=None):
	if request.method == "POST":
		form = RentalConfirmForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			if booking_id != None:
				booking = Booking.objects.get(id=booking_id)
				setattr(booking, 'startDay', data['startDay'])
				setattr(booking, 'endDay', data['endDay'])
				setattr(booking, 'price', data['price'])
				setattr(booking, 'rentalItem', RentalItem.objects.get(name=data['rentalItem']))
				setattr(booking, 'is_confirmed', True)
				booking.save()
				print("success")
				return redirect('calendar')
			#booking = Booking.objects.get(id=booking_id)
			#setattr(booking, 'is_confirmed', True)
			#booking.save()
	return redirect("calendar")

@staff_member_required
def staff_create_booking_view(request):
	context = {"page_title": 'Book Boat', 'form_error': False}

	# Get user list
	User = get_user_model()
	users_qs = User.objects.all()
	user_dict = {-1: 'Search Customers...'}
	for user in users_qs:
		user_dict[user.id] = '{0} {1}'.format(user.first_name, user.last_name)
	users = tuple(user_dict.items())

	# Get rental item list
	rentals_qs = RentalItem.objects.all()
	rental_dict = {}
	for rental in rentals_qs:
		rental_dict[rental.id] = rental.name
	rentals = tuple(rental_dict.items())

	# Handle form submission
	if request.method == 'POST':
		booking_form = StaffRentalBookingForm(request.POST, uqs=users_qs, rqs=rentals_qs)
		new_user_form = TempNewUserForm(request.POST)

		# Check to see if new user was implemented
		if (booking_form.is_valid()):
			# See if a new user was inputted
			if (new_user_form.is_valid()):
				# Create new user
				data = new_user_form.cleaned_data
				rand_pw = User.objects.make_random_password()
				user = User.objects.create_user(email=data['email'], first_name=data['first_name'], last_name=data['last_name'], phone=data['phone_number'], password=rand_pw)

				# Submit form with newly created user
				new_booking = booking_form.save(commit=False)
				new_booking.user = user
				new_booking.save()

				# Redirect to calendar view
				return redirect('calendar')
			else:
				# Save booking form as-is assuming an existing user was selected
				if booking_form.cleaned_data['user'] != None:
					b = booking_form.save(commit=False)
					# Automatically confirm booking upon creation
					setattr(b, 'is_confirmed', True)
					b.save()
					return redirect('calendar')
				else:
					# If a user was not selected, re-render new-user form with error message
					context['form_error'] = True
		else:
			context['form_error'] = True
	
	form = StaffRentalBookingForm(uqs=users_qs, rqs=rentals_qs)
	context['booking_form'] = form
	context['new_user_form'] = TempNewUserForm()
	return render(request, 'boats/new_booking.html', context)

# CALENDAR FUNCTIONS
# Helpers
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView(ListView):
	model = Booking
	template_name = 'boats/booking_cal.html'
	# success_url = reverse_lazy("calendar")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		# Unconfirmed bookings
		unconfirmed = Booking.objects.filter(is_confirmed=False)

		d = get_date(self.request.GET.get('month', None))
		cal = Calendar(d.year, d.month)
		cal.setfirstweekday(calendar.SUNDAY)
		html_cal = cal.formatmonth(withyear=True)
		context['page_title'] = 'Rental Management'
		context['calendar'] = mark_safe(html_cal)
		context['prev_month'] = prev_month(d)
		context['next_month'] = next_month(d)
		context['unconfirmed'] = unconfirmed
		context['unconfirmed_empty'] = unconfirmed.count() == 0
		context['rental_confirm_form'] = RentalConfirmForm()
		context['boatPrices'] = context['rental_confirm_form'].fields['rentalItem'].get_prices()
		return context

@staff_member_required
def get_confirmed_bookings(request):
	confirmed = Booking.objects.filter(is_confirmed=True)
	data = []
	for booking in confirmed:
		data.append({
			'name': booking.user.get_full_name(),
			'rentalItem': booking.rentalItem.name,
			'startDay': booking.startDay.strftime('%Y-%m-%d'),
			'endDay': booking.endDay.strftime('%Y-%m-%d'),
			'price': str(booking.price),
			'email': booking.user.email,
			'phone': booking.user.get_phone(),
			'pk': booking.pk
			})
	return JsonResponse({'data': data})

@staff_member_required
def manage_fleet_view(request):
	context= {'boatList': Boat.objects.all()}
	return render(request,'boats/manage_fleet.html', context)

@staff_member_required
def boat_form_view(request):
	if request.method == 'POST':
		form = rental_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('manage_fleet')
	else:
		print('not valid')
		form = rental_form()
	context = {
		'form' : form
		}
	return render(request, 'boats/boat_post_form.html', context)