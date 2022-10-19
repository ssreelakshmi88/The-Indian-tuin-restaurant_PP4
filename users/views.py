from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth \
    import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.forms import AuthenticationForm


def user_profile(request):
    """
    This view will render a user profile.
    This can only be accessed by registered and logged in users
    """
    if request.user.is_authenticated:
        user = User.objects.filter(username=request.user.username).first()
        
    return render(request, 'users/profile.html')
