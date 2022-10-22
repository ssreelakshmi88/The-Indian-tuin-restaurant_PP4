from django.urls import path
from . import views


app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations'),
    path('edit/reservations/<slug:slug>/',
         views.edit_user_reservation, name='edit_reservation'
         ),
    path('delete/<slug:slug>/',
         views.delete_user_reservation, name='delete_reservation'
         ),
]
