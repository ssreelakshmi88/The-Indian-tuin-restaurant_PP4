from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Menu, Category
from .forms import MenuForm


def handler404(request, exception):
    return render(request, 'error/404.html', status=404)


def handler500(request):
    return render(request, 'error/500.html', status=500)


def handler403(request, exception):
    return render(request, 'error/403.html', status=403)


def menu(request):
    """
    This view is to render menu items in the page.
    Each page will render 6 items per page.
    """
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
            messages.success(request, f'{menu_item.name} Updated.')
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
        messages.success(request, f'{menu_item.name} Deleted.')
        return redirect('menu')

    context = {'menu_item': menu_item}
    return render(request, 'menu/delete_menuitem.html', context)
