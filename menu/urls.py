from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('create_menu/', views.create_menu_item, name='create_menu'),
    path('edit_menu/<slug:slug>', views.edit_menu_item, name='edit_menu')
]