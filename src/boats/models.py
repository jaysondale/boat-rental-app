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

class RentalItem(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	dayPrice = models.DecimalField(max_digits=10, decimal_places=2)
	weekPrice = models.DecimalField(max_digits=10, decimal_places=2)
	startDay = models.DateField()
	endDay = models.DateField()

	def __str__(self):
		return self.name

class Boat(RentalItem):
	hp = models.IntegerField()
	capacity = models.IntegerField()

class Event(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	date = models.DateField()
	SPORTS = "Sports"
	ARTS = "Arts"
	FOOD = "Food"
	category_choices = [
		(SPORTS, 'Sports'),
		(ARTS, 'Arts'),
		(FOOD, 'Food')
	]
	category = models.CharField(choices=category_choices, max_length=10, default=SPORTS)





