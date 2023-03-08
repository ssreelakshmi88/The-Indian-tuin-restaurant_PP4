from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth \
    import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from restaurant.models import Reservation
from .models import UserProfile
from .forms import UserProfileForm, ContactForm
from django import forms
from django.conf import settings


def user_register(request):
    """
    This view is for registering new users.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'new user {user.username} was created.')
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def user_profile(request):
    """
    This view will render a user profile.
    This can only be accessed by registered and logged in users
    """
    user = User.objects.filter(username=request.user.username).first()
    profile = user.userprofile
    users = UserProfile.objects.all().count()
    if user.is_staff:
        reservations = Reservation.objects.all().count()
    else:
        reservations = Reservation.objects. \
                filter(email=request.user.email).count()
    likes = 0
    comments = 0
    posts = Post.objects.all()
    for post in posts:
        comments += post.comments.filter(name=request.user).count()

    user_comments = Comment.objects.filter(name=request.user).count()

    context = {
            'profile': profile,
            'users': users,
            'reservations': reservations,
            'comments': comments,
            'likes': likes,
            'user_comments': user_comments,

        }

    return render(request, 'users/profile.html', context=context)


@login_required
def edit_profile(request):
    """
    This view is for users to edit their profile.
    """
    user = UserProfile.objects.filter(
            username=request.user.username
        ).first()
    form = UserProfileForm(instance=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)

    if form.is_valid():
        form.save()
        messages.success(request, 'Profile is updated.')
        return redirect('profile')
    context = {'form': form, }
    return render(request, 'users/edit_profile.html', context)


@login_required
def delete_profile(request):
    """
    This view is for users to delete their profile.
    """
    user = UserProfile.objects.filter(
            username=request.user.username
        ).first()
    if request.method == 'POST':
        user.delete()
        logout(request)
        messages.success(request, 'Profile Deleted.')
        return redirect('home')

    context = {'user': user}
    return render(request, 'users/delete_profile.html')


def contact(request):
    """
    This view is to render contact page.
    """
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email_data = form.cleaned_data
            con = get_connection(
                'django.core.mail.backends.console.EmailBackend'
                )
            send_mail(
                subject="Email Form",
                message=email_data['message'],
                from_email=email_data['email_address'],
                recipient_list=['your-email@example.com'],
                connection=con
            )
            messages.success(request, 'Message sent')
            return redirect('contact')
            messages.success(request, 'Message sent')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'users/contact.html', {"form": form,
                  'submitted': submitted})
