from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('create_menu/', views.create_menu_item, name='create_menu'),
    path('edit_menu/<slug:slug>', views.edit_menu_item, name='edit_menu'),
    path('delete_menu/<slug:slug>', views.delete_menu_item, name='delete_menu'),
]