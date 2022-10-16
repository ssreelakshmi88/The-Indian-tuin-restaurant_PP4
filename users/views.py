from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile


def user_login(request):
    page = login
    context = {'page': page,}
    return render(request, 'users/login.html', context)