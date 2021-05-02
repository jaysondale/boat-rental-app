from django.shortcuts import render
from datetime import date, timedelta, datetime
from user_manage.models import User
from boats.models import RentalItem
from .models import StoreHour

# Create your views here.
def contact_view(request):
	stores = StoreHour.objects.all()
	context = {
		'page_title': 'Contact',
		'stores': stores,
		'default': 'Store - Spring'
	}
	# Determine whether to set spring or summer as default
	month = date.today().month
	# If July or August, use summer hours
	if (month == 7 or month == 8):
		context['default'] = 'Store - Summer'

	return render(request, 'pages/contact.html', context)

def services_view(request):
	context = {
		'page_title': 'Services'
	}
	return render(request, 'pages/services.html', context)

def home_view(request):
	# Pick first 3 rental items
	rentals = RentalItem.objects.all()
	context = {
		'boats': rentals,
		'page_title': 'Home'
	}

	return render(request, "pages/main.html", context)

def store_view(request):
	context = {
		'page_title': 'Store'
	}
	return render(request, "pages/store.html", context)

def food_view(request):
	context = {
		'page_title': 'Food & Beverage'
	}
	return render(request, "pages/food.html", context)

