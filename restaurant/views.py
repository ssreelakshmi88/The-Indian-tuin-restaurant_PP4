from django.shortcuts import render, redirect
from .models import Photo, Reservation
from .forms import ReservationForm
from django.contrib import messages
from datetime import datetime


def home(request):
    banner_image = Photo.objects.get(title='banner_image')
    about_image = Photo.objects.get(title='about_image')
    logo_image = Photo.objects.get(title='indian tuin_logo')
    context = {
        'banner_image': banner_image,
        'about_image': about_image}
    return render(request, 'home/index.html', context)


def reservations(request):
    """
    This view will render the reservations page
    """

    time_image = Photos.object.get(title='Times Image')
    form = ReservationForm()

