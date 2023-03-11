from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photo, Reservation
from .forms import ReservationForm
from django.contrib.auth import get_user_model


def handler404(request, exception):
    return render(request, 'error/404.html', status=404)


def handler500(request):
    return render(request, 'error/500.html', status=500)


def home(request):
    """
    This view will render the images of the home page.
    """
    about_image = Photo.objects.get(title='about_image')
    context = {
        'about_image': about_image}
    return render(request, 'restaurant/index.html', context)


User = get_user_model()


def reservations(request):
    """
    This view will render the reservations page
    """
    time_image = Photo.objects.get(title='Times Image')
    if request.user.is_authenticated:
        form = ReservationForm()
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            date = form['date'].value()
            date_value = datetime.strptime(date, "%Y-%m-%d")
            time = form['time'].value()
            reservation = Reservation.objects. \
                filter(date=date_value, time=time)
            # Check if the restaurant is closed on Mondays
            if date_value.weekday() == 0:
                messages.warning(request,
                                 'Sorry, the restaurant is closed on Mondays.'
                                 )

                return redirect('reservations')
            if reservation:
                messages.warning(
                    request,
                    'Reservation already exists at this date and time.'
                    'Please choose another date and time'
                    )
                return redirect('reservations')
            if form.is_valid():
                form.save()
                messages.success(request, 'Reservation created successfully.')
                return redirect('reservations_success')
            else:
                messages.error(request, f'Some details are missing/wrong.')
        context = {
            'time_image': time_image,
            'form': form
        }
        return render(request, 'restaurant/reservations.html', context)
    else:
        form = ReservationForm()
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                date = form['date'].value()
                date_value = datetime.strptime(date, "%Y-%m-%d")
                time = form['time'].value()
                email = form['email'].value()
                reservation = Reservation.objects. \
                    filter(date=date_value, time=time)
                # Check if the restaurant is closed on Mondays
                if date_value.weekday() == 0:
                    messages.warning(request,
                                     'Sorry, the restaurant closed on Mondays.'
                                     )

                    return redirect('reservations')
                if reservation:
                    messages.warning(
                        request,
                        'Reservation already exists at this date and time.'
                        'Please choose another date and time'
                        )
                    return redirect('reservations')
                reservation = Reservation.objects.create(
                    date=date_value,
                    time=time,
                    email=email
                )
                reservation.save()
                messages.success(request, 'Reservation created successfully.')
                return redirect('reservations_success')
            else:
                messages.error(request, f'Some details are missing/wrong.')
        context = {'time_image': time_image, 'form': form}
        return render(request, 'restaurant/reservations.html', context)


def reservations_success(request):
    """
    This view will render the reservations success page
    """
    return render(request, 'restaurant/reservations_success.html')


@login_required
def edit_user_reservation(request, pk):
    """
    This view allows the user to edit reservations.
    """
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)

    if request.method == 'POST':
        form = ReservationForm(
            request.POST, request.FILES, instance=reservation
            )
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            # Check if there is already a reservation for this date and time
            if Reservation.objects.filter(date=date, time=time).exists():
                messages.warning(
                 request,
                 'Reservation already exists at this date and time.'
                 'Please choose another date and time'
                )
                return redirect('user_reservations')

            # Check if the restaurant is closed on Mondays
            if date.weekday() == 0:
                messages.warning(
                    request,
                    'Sorry, the restaurant is closed on Mondays.'
                    )
                return redirect('user_reservations')

            # Save the reservation if everything is valid
            form.save()
            messages.success(request, 'Reservation Updated.')
            return redirect('user_reservations')

    context = {'form': form}
    return render(request, 'restaurant/edit_reservation.html', context)


@login_required
def delete_user_reservation(request, pk):
    """
    This view allows the user to delete reservations.
    """
    reservation = Reservation.objects.get(id=pk)

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation has been deleted.')
        redirect('user_reservations')

    context = {'reservation': reservation}
    return render(request, 'restaurant/delete_reservation.html', context)


@login_required
def user_reservations(request):
    """
    This view allows the user to see their reservations.
    """

    reservations = Reservation.objects.all()

    if request.user.is_staff:
        user_reservations = reservations.order_by('date')
        if not user_reservations:
            messages.warning(request, 'No Reservations Booked At This Time.')
            return render(request, 'users/profile.html')
    else:
        user_reservations = reservations.filter(
            email=request.user.email
            ).order_by('date')
        if not user_reservations:
            messages.warning(request, 'No Reservations Found For This Email.')
            return render(request, 'users/profile.html')
    context = {'reservations': user_reservations}
    messages.success(request, 'Reservations Found.')
    return render(request, 'restaurant/user_reservations.html', context)
