from django.db import models

# Create your models here.
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