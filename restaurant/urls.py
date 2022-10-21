from django.urls import path
from . import views


app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/',
         views.edit_user_reservation, name='edit_user_reservation'
         ),
    path('reservations/',
         views.delete_user_reservation, name='delete_user_reservation'
         ),
]
