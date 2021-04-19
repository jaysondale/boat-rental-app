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
from user_manage import views as user_views
from datetime import datetime

class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str):
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value: datetime.date):
        return value.strftime('%Y-%m-%d')

register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('', boat_views.boat_detail_view, name='main'),
    path('marine/', boat_views.marine_view, name='marine'),
    path('events/', boat_views.events_view, name='events'),
    path('events/<event_id>', boat_views.event_filter, name='events_filter'),
    path(r'events/(?P<event_id>[0-9]+)/$', boat_views.event_interested, name='events_interested'),
    path('contact/', boat_views.contact_view, name='contact'),
    path('activities/', boat_views.activities_view, name='activities'),
    path('activities/land', boat_views.land_activities_view, name='land_activities'),
    path('activities/water', boat_views.water_activities_view, name='water_activities'),
    path('activities/water/boat_post_form', boat_views.boat_form_view, name='boat_post_form'),
    path('all_bookings/', boat_views.all_bookings_view, name='all_bookings_view'),
    path('all_bookings/<yyyy:new_date>/', boat_views.all_bookings_view, name='all_bookings_view'),
    path('bookings/', boat_views.bookings_view, name='bookings'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'^signup/$', user_views.signup, name='signup'),
    path(r'delete/(?P<booking_id>[0-9]+)/$', boat_views.delete_booking, name='delete'),
    path('activities/water/book_boat/(?P<boat_id>[0-9]+)/$', boat_views.book_boat, name='book_boat'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
