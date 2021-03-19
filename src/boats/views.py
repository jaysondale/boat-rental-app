from django.shortcuts import render

from .models import Boat
# Create your views here.
def boat_detail_view(request):
	boats = Boat.objects.all()
	context = {
		'page_title': 'KLM Boat Rentals',
		'boats': boats
	}
	return render(request, "boats/main.html", context)