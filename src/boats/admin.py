from django.contrib import admin

from .models import Boat, Booking, Event

admin.site.register(Boat)
admin.site.register(Booking)
admin.site.register(Event)
