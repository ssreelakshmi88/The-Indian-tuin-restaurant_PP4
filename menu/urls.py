from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('create_menu/', create_menu_item, name='menu')
]