from django.db import models
from colorfield.fields import ColorField
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')
DEFAULT_CATEGORY = 1

# Create your models here.

class Booking(models.Model):
	startDay = models.DateField()
	endDay = models.DateField()
	rentalItem = models.ForeignKey('RentalItem', on_delete=models.CASCADE)
	user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_confirmed = models.BooleanField(default=False)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	# Default price for unconfirmed bookings
	DEFAULT_PRICE = -1

class RentalCategory(models.Model):
	name = models.CharField(max_length=120, null=False, primary_key=True)

class RentalItem(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to='images')
	dayPrice = models.DecimalField(max_digits=10, decimal_places=2)
	weekPrice = models.DecimalField(max_digits=10, decimal_places=2)
	color = ColorField(default='#90EE90')
	hp = models.IntegerField(null=True)
	capacity = models.IntegerField()
	category = models.ForeignKey(RentalCategory, null=True, blank=True, on_delete=models.RESTRICT)

	def __str__(self):
		return self.name