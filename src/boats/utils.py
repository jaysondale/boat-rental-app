from datetime import datetime, timedelta
from calendar import HTMLCalendar

from .models import Booking

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	def formatday(self, day, bookings):
		bookings_per_day = bookings.filter(startDay__day=day)
		d = ''
		for booking in bookings_per_day:
			d += f'<li class="calendar_list">{booking.rentalItem}</li>'
		if day != 0:
			return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
		return '<td></td>'

	def formatweek(self, theweek, bookings):
		week = ''
		for d, weekday, in theweek:
			week += self.formatday(d, bookings)
		return f'<tr>{week}</tr>'

	def formatmonth(self, withyear=True):
		bookings = Booking.objects.filter(startDay__year=self.year, startDay__month=self.month)
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, bookings)}\n'
		return cal + '</table>'