from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Menu, Category


def menu(request):
    menu = Menu.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'menu': menu, 'categories': categories, 'page_obj': page_obj, }
    
    return render(request, 'menu/menu.html', context)
