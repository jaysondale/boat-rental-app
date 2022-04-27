from django.contrib import admin

from .models import RentalItem, Booking, RentalCategory

admin.site.register(RentalCategory)
admin.site.register(RentalItem)
admin.site.register(Booking)
