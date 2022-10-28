from django.urls import path
from . import views


urlpatterns = [
      path('contact', views.contact, name='contact'),
      path('profile/', views.user_profile, name='profile'),
      path('register/', views.user_register, name='register'),
      path('profile/edit/', views.edit_profile, name='edit_profile'),
      path('profile/delete/', views.delete_profile, name='delete_profile'),
]