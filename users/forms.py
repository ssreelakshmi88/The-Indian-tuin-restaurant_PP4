from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from . models import UserProfile


class UserProfileForm(UserCreationForm):
    email = forms.EmailField(required=True)
    """
    This form class defines the output of the user form for the user profile
    """
    class Meta:
        """
        The meta class determines the fields accessible to the user
        """
    model = UserProfile
    fields = ['name', 'username', 'email', 'profile_image', ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, required=True)
