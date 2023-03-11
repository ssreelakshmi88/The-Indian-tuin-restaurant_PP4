from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from . models import UserProfile, Contact


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

        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
        }


class ContactForm(forms.ModelForm):
    """
    This form class defines contact form
    """
    name = forms.CharField(max_length=50, label="Name", required=True)
    email_address = forms.EmailField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        """
        The meta class determines the fields accessible to the user
        """
        model = Contact
        fields = ['name', 'email_address', 'message', ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'required': True,
                    "class": "form-control",
                    "pattern": "[A-Za-z ]+",
                    "title": "Name can only contain letters",
                }
            ),
            'email_address': forms.TextInput(
                attrs={
                    'required': True,
                    "class": "form-control",
                    "pattern": '[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,}$',
                    "title": "Please enter a valid email address",
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'required': True,
                    "class": "form-control",
                    "pattern": r'^[A-Za-z0-9!@#$%^&*()_+{}\[\]:;"\'\\s]+$',
                    "title": "Please enter a valid message",
                }
            ),
        }
