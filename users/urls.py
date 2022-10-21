from django.urls import path
from . import views


urlpatterns = [
      path('profile/', views.user_profile, name='profile'),
      path('register/', views.user_register, name='register'),
      
]