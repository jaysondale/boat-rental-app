from django.shortcuts import render
from user_manage.models import User

# Create your views here.
def contact_view(request):
	context = {
		'page_title': 'Contact'
	}
	return render(request, 'pages/contact.html', context)

def services_view(request):
	context = {
		'page_title': 'Services'
	}
	return render(request, 'pages/services.html', context)

def home_view(request):
	context = {
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

