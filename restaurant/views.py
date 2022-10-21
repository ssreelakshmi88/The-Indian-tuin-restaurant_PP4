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

    time_image = Photo.objects.get(title='Times Image')
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('reservations'))
        else:
            messages.error(request, 'There was an error with your form.')
    context = {
        'time_image': time_image,
        'form': form
    }
    return render(request, 'home/reservations.html', context)


@login_required
def edit_user_reservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)

    if request.method == 'POST':
        form = ReservationForm(
            request.POST, request.FILES,
            instance=reservation
            )
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation Updated.')

    context = {'form': form}
    return render(request, 'restaurant/edit_reservation.html', context)


@login_required
def delete_user_reservation(request, pk):
    reservation = Reservation.objects.get(id=pk)

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation has been deleted.')

    context = {'reservation': reservation}
    return render(request, 'restaurant/delete_reservation.html', context)

        
