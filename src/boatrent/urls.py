"""boatrent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, register_converter
from django.conf.urls.static import static
from django.conf import settings
from boats import views as boat_views
from boats.views import CalendarView
from user_manage import views as user_views
from pages import views as pages_views
from events import views as event_views
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required

class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str):
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value: datetime.date):
        return value.strftime('%Y-%m-%d')

register_converter(DateConverter, 'yyyy')

"""path('profile/email/', user_views.profile_view_email, name='profile_email'),
    path('profile/fname/', user_views.profile_view_fname, name='profile_fname'),
    path('profile/lname/', user_views.profile_view_lname, name='profile_lname'),
    path('profile/phone/', user_views.profile_view_phone, name='profile_phone'),"""

urlpatterns = [
    path('', pages_views.home_view, name='main'),
    path('services/', pages_views.services_view, name='services'),
    path('profile/<form_url>', user_views.profile_view_form, name='profile'),
    path('food-beverage/', pages_views.food_view, name='food'),
    path('store/', pages_views.store_view, name='store'),
    path('events/', event_views.events_view, name='events'),
    path('events/add', event_views.event_add, name='add_event'),
    path('events/<filter_kw>', event_views.event_filter, name='events_filter'),
    path(r'events/interested/(<event_id>[0-9]+)/', event_views.event_interested, name='events_interested'),
    path('contact/', pages_views.contact_view, name='contact'),
    path('rentals/', boat_views.rentals_view, name='water_activities'),
    path('rentals/boat_post_form', boat_views.boat_form_view, name='boat_post_form'),
    path('upcoming_rentals/', boat_views.upcoming_rentals_view, name='upcoming_rentals_view'),
    path('upcoming_rentals/<yyyy:new_date>/', boat_views.upcoming_rentals_view, name='upcoming_rentals_view'),
    path('bookings/', boat_views.bookings_view, name='bookings'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'signup/', user_views.signup, name='signup'),
    path(r'delete/(<booking_id>[0-9]+)/', boat_views.user_delete_booking, name='delete'),
    path(r'activities/water/book_boat/(<boat_id>[0-9]+)/', boat_views.book_boat, name='book_boat'),
    path('admin/', admin.site.urls),
    path('manage_rental_bookings/', staff_member_required(CalendarView.as_view()), name='calendar'),
    path(r'manage_rental_bookings/confirm_booking/(<booking_id>[0-9]+)/', boat_views.confirm_booking, name='confirm_booking'),
    path(r'manage_rental_bookings/delete_booking/(<booking_id>[0-9]+)/', boat_views.staff_delete_booking, name='staff_delete_booking'),
    path('manage_rental_bookings/create_booking', boat_views.staff_create_booking_view, name='staff_create_booking_view'),
    path(r'manage_rental_bookings/get_booking_data/<int:booking_id>', boat_views.get_booking_data, name='get_booking_data')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
