from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    This form class defines the output of the user form for the user profile
    """
    class Meta:
        """
        The meta class determines the fields accessible to the user
        """
    model = UserProfile
    fields = ['name', 'username', 'email', 'profile_image', ]