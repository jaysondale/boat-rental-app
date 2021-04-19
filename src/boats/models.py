from django.db import models
from django.forms import ModelForm
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.

class Booking(models.Model):
	startDay = models.DateField()
	endDay = models.DateField()
	rentalItem = models.ForeignKey('RentalItem', on_delete=models.CASCADE)
	user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta:
		permissions = [
			("view_all_system_bookings", "Can view bookings made by all system users")
		]

class RentalItem(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to='images')
	dayPrice = models.DecimalField(max_digits=10, decimal_places=2)
	weekPrice = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name

class Boat(RentalItem):
	hp = models.IntegerField()
	capacity = models.IntegerField()

class Event(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	date = models.DateField()
	startTime = models.TimeField()
	endTime = models.TimeField()
	Interested = models.IntegerField(default=0)
	SPORTS = "Sports"
	ARTS = "Arts"
	FOOD = "Food"
	NA = 'NA'
	category_choices = [
		(SPORTS, 'Sports'),
		(ARTS, 'Arts'),
		(FOOD, 'Food'),
		(NA, 'NA')
	]
	category = models.CharField(choices=category_choices, max_length=10, default=NA)





