from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Menu


def menu(request):
    menu = Menu.objects.all()
    context = {'menu': menu, }
    return render(request, 'menu/menu.html', context)

