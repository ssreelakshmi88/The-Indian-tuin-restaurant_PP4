from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth \
    import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def user_register(request):
    if request.method == 'GET':
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
    user = User.objects.filter(username=request.user.username).first()
    profile = user.userprofile
    context = {
            'profile': profile,
              }
    return render(request, 'users/profile.html', context=context)


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email_address'],
                    'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(message, admin@gamil.com, ["laxmi@gamil.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return messages.success(request, 'Message sent')
    form = ContactForm()
    return render(request, "users/contact.html", {"form": form})
