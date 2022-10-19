from django.urls import path
from . import views


app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations')
]
