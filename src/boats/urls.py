from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_rental_form, name='item_rental_form'),
]