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


class ContactForm(forms.ModelForm):
    """
    This form class defines contact form
    """
    name = forms.CharField(max_length=50, label="Your Name")
    email_address = forms.EmailField(max_length=150, required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_email(self):
        email_address = self.cleaned_data.get('email_address')
        if not email_address.endswith('example.com'):
            raise forms.ValidationError('Invalid email address')
        return email_address

    class Meta:
        """
        The meta class determines the fields accessible to the user
        """
        model = Contact
        fields = ['name', 'email_address', 'message', ]
