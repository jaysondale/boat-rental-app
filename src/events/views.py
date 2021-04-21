from django.shortcuts import render, redirect
from django.db.models import F
from .forms import event_form

from .models import Event

# Create your views here.
def events_view(request):
	events = Event.objects.all()
	
	context = {
		'page_title': "Events",
		'events': events
	}
	return render(request, 'events/events.html', context)

# move these logic into separate functions

def event_filter(request, event_id=None, event_pk=None):

	# filter functionality
	if event_id == 'Arts':
		events = Event.objects.filter(category='Arts')
	elif event_id == 'Sports':
		events = Event.objects.filter(category='Sports')
	elif event_id == 'Food':
		events = Event.objects.filter(category='Food')
	else:
		events = Event.objects.all()

	context = {
		'events': events
	}

	return render(request, 'events/events.html', context)

def event_interested(request, event_id=None):
	Event.objects.filter(pk=event_id).update(Interested=F('Interested') + 1)
	return redirect("events")

def event_add(request):
	if request.method == 'POST':
		form = event_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('events')
	else:
		print('not valid')
		form = event_form()

	context = {
		'page_title': 'New Event',
		'form' : form
	}

	return render(request, 'events/event_form.html', context)


