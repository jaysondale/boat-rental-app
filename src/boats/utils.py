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

	def formatday(self, day, bookings, bookings_week_s_edge, bookings_week_e_edge, d_index, bookings_order):
		if day != 0:
			bookings_per_day = bookings.filter(startDay__day__lte=day, endDay__day__gte=day)
			if not bookings_week_s_edge == None:
				bookings_per_day = bookings_per_day | bookings_week_s_edge.filter(endDay__day__gte=day)
			if not bookings_week_e_edge == None:
				bookings_per_day = bookings_per_day | bookings_week_e_edge.filter(startDay__day__lte=day)
			d = ''
			order = {}
			order_keys = []
			for booking in bookings_per_day:
				if bookings_order[booking] == None:
					bookings_order[booking] = self._getLowestAvailable(bookings_order)
				key = bookings_order[booking]
				order[key] = booking
				order_keys.append(key)

			if (len(order_keys) > 0):
				for order_index in range(max(order_keys) + 1):
					if order_index in order_keys:
						booking = order[order_index]
						c_status = 'confirmed' if booking.is_confirmed else 'pending'
						label = f'{booking.rentalItem} - {booking.user.get_full_name()}' if d_index == 0 or booking.startDay.day == day or day == 1 else '&nbsp;'
						
						d += f'<li class="calendar_list title {c_status}">{label}</li>'
					else:
						d += f'<li class="calendar_list blank">&nbsp;</li>'
			
			for booking in bookings_per_day:
				if (booking.endDay.day == day):
					bookings_order[booking] = None
			return f"<td><span class='date pl-2'>{day}</span><ol>{d}</ol></td>"
		return '<td></td>'

	def formatweek(self, theweek, month, year, bookings):
		firstDay = theweek[0][0]
		lastDay = theweek[6][0]

		bookings_week_s_edge = None
		bookings_week_e_edge = None
		# If week includes days from previous month
		if (0,0) in theweek:
			# Bookings with endDay this month, but startDay last month
			bookings_week_s_edge = bookings.filter(endDay__month=month, startDay__month=(month-1 if month > 0 else 11))
		elif (0, 6) in theweek:
			# Bookings with startDay this month, but endDay next month
			bookings_week_e_edge = bookings.filter(startDay__month=month, endDay__month=(month+1 if month < 11 else 0))

		bookings_week_a = bookings.filter(endDay__day__gte=firstDay, startDay__day__lte=lastDay)

		# Weed out duplicates
		bookings_week = bookings_week_a.distinct()

		# Create bookings order
		bookings_sets = [bookings_week, bookings_week_s_edge, bookings_week_e_edge]
		bookings_order = {}
		for bookingSet in bookings_sets:
			if (bookingSet != None):
				for booking in bookingSet:
					bookings_order[booking] = None

		week = ''
		for d, weekday, in theweek:
			week += self.formatday(d, bookings_week, bookings_week_s_edge, bookings_week_e_edge, weekday, bookings_order)
		return f'<tr>{week}</tr>'

	def formatmonth(self, withyear=True):
		# Bookings that start this month
		bookings_a = Booking.objects.filter(startDay__year=self.year, startDay__month=self.month)
		# Bookings that end this month
		bookings_b = Booking.objects.filter(endDay__year=self.year, endDay__month=self.month)
		# Merge and find distinct set
		bookings_c = bookings_a | bookings_b
		bookings = bookings_c.distinct()


		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, self.month, self.year, bookings)}\n'
		return cal + '</table>'