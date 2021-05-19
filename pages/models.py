from django.db import models

# Create your models here.
class StoreHour(models.Model):
	name = models.CharField(max_length=120)
	monday = models.CharField(max_length=120)
	tuesday = models.CharField(max_length=120)
	wednesday = models.CharField(max_length=120)
	thursday = models.CharField(max_length=120)
	friday = models.CharField(max_length=120)
	saturday = models.CharField(max_length=120)
	sunday = models.CharField(max_length=120)

	decoder = {
		0: sunday,
		1: monday,
		2: tuesday,
		3: wednesday,
		4: thursday,
		5: friday,
		6: saturday
	}

	def getHours(self, weekday):
		return decoder[weekday]