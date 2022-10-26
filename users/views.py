from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth \
    import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, get_connection
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Comment
from restaurant.models import Reservation
from django.contrib.auth.decorators import login_required


def user_register(request):
    """
    This view is for regsitering new users.
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
            return redirect('register')
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
    approvals = Comment.objects.filter(approved=False).count()
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
        likes += post.likes.filter(username=request.user.username).count()
        reservations += Reservation.objects.filter(email=request.user.email).count()
        
        context = {
            'profile': profile,
            'users': users,
            'reservations': reservations,
            'comments': comments,
            'likes': likes,
            'approvals': approvals,
        }
        return render(request, 'users/profile.html', context=context)


@login_required
def edit_profile(request):
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
    user = UserProfile.objects.filter(
            username=request.user.username
        ).first()
    if request.method == 'POST':
        user.delete()
        logout(request)
        messages.success(request, 'Profile Deleted.')
        return redirect('restaurant:home')

    context = {'user': user}
    return render(request, 'users/delete_profile.html')


def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email_data = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                subject="Email Form",
                message=email_data['message'],
                from_email='siteowner@example.com',
                recipient_list=[email_data['email_address']],
                connection=con
            )
            messages.success(request, 'Message sent')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'users/contact.html', {"form": form, 'submitted': submitted})
