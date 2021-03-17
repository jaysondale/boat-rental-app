from django.shortcuts import render

from .models import Boat
# Create your views here.
def boat_detail_view(request):
	obj = Boat.objects.get(id=1)
	context = {
		'page_title': 'KLM Boat Rentals',
		'object': obj
	}
	return render(request, "boats/main.html", context)