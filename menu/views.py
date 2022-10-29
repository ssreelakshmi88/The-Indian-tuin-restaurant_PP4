from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Menu, Category
from .forms import MenuForm


def menu(request):
    menu = Menu.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'menu': menu, 'categories': categories, 'page_obj': page_obj, }

    return render(request, 'menu/menu.html', context)


def create_menu_item(request):
    """
    This view a form to create menu items.
    """
    form = MenuForm()

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item is created.')
            return redirect('menu')

    context = {'form': form}
    return render(request, 'menu/menu_form.html', context)


def edit_menu_item(request, slug):
    """
    This view that renders a form to edit menu items.
    """
    menu_item = Menu.objects.get(slug=slug)
    form = MenuForm(instance=menu_item)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, f'{menu_item.title} Updated.')
            return redirect('menu')

    context = {'form': form}
    return render(request, 'menu/menu_form.html', context)


def delete_menu_item(request, slug):
    """
    This view renders a form to delete menu items.
    """
    menu_item = Menu.objects.get(slug=slug)

    if request.method == 'POST':
        menu_item.delete()
        messages.success(request, f'{menu_item.title} Deleted.')
        return redirect('menu')

    context = {'menu_item': menu_item}
    return render(request, 'menu/delete_menuitem.html', context)
