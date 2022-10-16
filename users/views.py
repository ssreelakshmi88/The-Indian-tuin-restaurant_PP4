from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth \
    import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
    page = 'login'
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    f"You are now logged in as {username}."
                    )
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    context = {'page': page, 'form': form, }
    return render(request, 'users/login.html', context)


def user_register(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            if User.objects.filter(username=user.username):
                messages.error(
                    request, 'Username exists, '
                    'please try a different username.')
                return HttpResponseRedirect('register')

            else:
                user.save()

            messages.success(request, f'new user {user.username} was created.')
            return redirect('login')

            context = {'page': page, 'form': form}
            return render(request, 'users/register.html', context)
