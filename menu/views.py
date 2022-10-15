from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Menu


def menu(request):
    menu = Menu.objects.all()
    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'menu': menu, 'page_obj': page_obj, }
    return render(request, 'menu/menu.html', context)
