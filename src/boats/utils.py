from datetime import datetime, timedelta, date
from calendar import HTMLCalendar, SUNDAY

from .models import Booking

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	def _getLowestAvailable(self, bookings_order):
		# Sorted indicies
		indexlist = []
		for key in bookings_order.keys():
			if bookings_order[key] != None:
				indexlist.append(bookings_order[key])
		min_index = 0
		if len(indexlist) > 0:
			indexlist.sort()
			for index in indexlist:
				if index == min_index:
					min_index += 1
		return min_index

	def formatday(self, day, bookings, d_index, bookings_order):
		# Ensure booking is valid this month (day > 0)
		if day != 0:
			# Create date object for current day
			today = date(self.year, self.month, day)
			# Find all events spanning current day
			bookings_per_day = bookings.filter(startDay__lte=today, endDay__gte=today)
			# Create day html string
			d = ''
			order = {}
			order_keys = []
			# Create rendering order dictionary
			for booking in bookings_per_day:
				if bookings_order[booking] == None:
					bookings_order[booking] = self._getLowestAvailable(bookings_order)
				key = bookings_order[booking]
				order[key] = booking
				order_keys.append(key)

			# Iterate through each order index and display event block
			if (len(order_keys) > 0):
				for order_index in range(max(order_keys) + 1):
					if order_index in order_keys:
						booking = order[order_index]
						c_status = 'confirmed' if booking.is_confirmed else 'pending'
						edge_class = ''
						if (booking.endDay == today):
							if (booking.startDay == today):
								edge_class = 'start-end-day'
							else:
								edge_class = 'end-day'
						elif (booking.startDay == today):
							edge_class = 'start-day'

						label = f'{booking.rentalItem} - {booking.user.get_full_name()}' if d_index == SUNDAY or booking.startDay.day == day or day == 1 else '&nbsp;'
						
						d += f'<li class="calendar_list title {edge_class} {c_status}">{label}</li>'
					else:
						d += f'<li class="calendar_list blank">&nbsp;</li>'
			
			for booking in bookings_per_day:
				if (booking.endDay.day == day):
					bookings_order[booking] = None
			return f"<td><span class='date pl-2'>{day}</span><ol>{d}</ol></td>"
		return '<td></td>'

	def formatweek(self, theweek, month, year, bookings):
		# Create date object for first and last days of the month
		firstDay_day = 0
		lastDay_day = 0
		# Iterate through days until valid day found
		for d, wd in theweek:
			if (d > 0):
				firstDay_day = d
				break
		for d, wd in reversed(theweek):
			if (d > 0):
				lastDay_day = d
				break

		firstDay = date(year,month,firstDay_day)
		lastDay = date(year,month,lastDay_day)

		# Find bookings with days this week
		bookings_week = bookings.filter(startDay__lte=lastDay, endDay__gte=firstDay)

		# Create dictionary -> {booking: order}
		bookings_order = {}
		for booking in bookings_week:
			bookings_order[booking] = None

		# Format week html string
		week = ''
		for d, weekday, in theweek:
			week += self.formatday(d, bookings_week, weekday, bookings_order)
		return f'<tr>{week}</tr>'

	def formatmonth(self, withyear=True):
		# Query all bookings
		bookings = Booking.objects.all()

		# Format calendar html string
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, self.month, self.year, bookings)}\n'
		return cal + '</table>'