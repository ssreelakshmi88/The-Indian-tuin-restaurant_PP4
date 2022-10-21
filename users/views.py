from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth \
    import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.forms import AuthenticationForm


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'new user {user.username} was created.')
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_profile(request):
    """
    This view will render a user profile.
    This can only be accessed by registered and logged in users
    """
    if request.user.is_authenticated:
        user = User.objects.filter(username=request.user.username).first()
        users = UserProfile.objects.all().count()
        return render(request, 'users/profile.html')
