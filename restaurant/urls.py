from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations'),
    path(
        'reservations/user/',
        views.user_reservations,
        name='user_reservations'
        ),
    path('reservations/user/<int:pk>',
         views.edit_user_reservation, name='editReservations'
         ),
    path('reservations/user/<int:pk>/delete',
         views.delete_user_reservation, name='deleteReservations'
         ),
    path('reservations/success/',
         views.reservations_success, name='reservations_success'
         ),

]
