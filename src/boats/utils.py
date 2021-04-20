from datetime import datetime, timedelta
from calendar import HTMLCalendar

from .models import Booking

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	def _getLowestAvailable(self, bookings_order):
		min_index = 0
		for key in bookings_order.keys():
			if bookings_order[key] != None:
				if bookings_order[key] == min_index:
					min_index += 1
		return min_index

	def formatday(self, day, bookings, d_index, bookings_order):
		if day != 0:
			bookings_per_day = bookings.filter(startDay__day__lte=day, endDay__day__gte=day)
			d = ''
			order = {}
			order_keys = []
			for booking in bookings_per_day:
				if bookings_order[booking] == None:
					bookings_order[booking] = self._getLowestAvailable(bookings_order)
				key = bookings_order[booking]
				order[key] = booking
				order_keys.append(key)
				# d += f'<li class="calendar_list {c_status}">{label}</li>'
			print(order_keys)
			if (len(order_keys) > 0):
				for order_index in range(max(order_keys) + 1):
					if order_index in order_keys:
						c_status = 'confirmed' if order[order_index].is_confirmed else 'pending'
						label = f'{booking.rentalItem} - {booking.user.get_full_name()}' if d_index == 0 or booking.startDay.day == day else '&nbsp;'
						d += f'<li class="calendar_list title {c_status}">{label}</li>'
					else:
						d += f'<li class="calendar_list blank">&nbsp;</li>'
			
			for booking in bookings_per_day:
				if (booking.endDay.day == day):
					bookings_order[booking] = None
			return f"<td><span class='date pl-2'>{day}</span><ol>{d}</ol></td>"
		return '<td></td>'

	def formatweek(self, theweek, bookings):
		firstDay = theweek[0][0]
		lastDay = theweek[6][0]
		bookings_week_a = bookings.filter(endDay__day__gte=firstDay, startDay__day__lte=lastDay)
		bookings_week = bookings_week_a.distinct()
		bookings_order = {}
		for booking in bookings_week:
			bookings_order[booking] = None
		week = ''
		for d, weekday, in theweek:
			week += self.formatday(d, bookings_week, weekday, bookings_order)
		return f'<tr>{week}</tr>'

	def formatmonth(self, withyear=True):
		bookings = Booking.objects.filter(startDay__year=self.year, startDay__month=self.month)
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, bookings)}\n'
		return cal + '</table>'