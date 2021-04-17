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
from django.urls import path
from django.urls import path, include
from boats import views

urlpatterns = [
    path('', views.boat_detail_view, name='main'),
    path('marine/', views.marine_view, name='marine'),
    path('events/', views.events_view, name='events'),
    path('events/<event_id>', views.events_view, name='events_filter'),
    path('contact/', views.contact_view, name='contact'),
    path('activities/', views.activities_view, name='activities'),
    path('activities/land', views.land_activities_view, name='land_activities'),
    path('activities/water', views.water_activities_view, name='water_activities'),
    path('activities/water/boat_post_form', views.boat_form_view, name='boat_post_form'),
    path('bookings/', views.bookings_view, name='bookings'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'^signup/$', views.signup, name='signup'),
    path(r'delete/(?P<booking_id>[0-9]+)/$', views.delete_booking, name='delete'),
    path('activities/water/book_boat/(?P<boat_id>[0-9]+)/$', views.book_boat, name='book_boat'),
    path('admin/', admin.site.urls)
]
