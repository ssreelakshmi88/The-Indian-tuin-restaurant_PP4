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
    name = forms.CharField(max_length=50, label="Your Name")
    email_address = forms.EmailField(max_length=150, required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_email_address(self):
        email_address = self.cleaned_data.get('email_address')
        if email_address and not email_address.endswith('example.com'):
            raise forms.ValidationError('Invalid email address')
        return email_address

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError('Name should only contain alphabets')
        return name

    def clean(self):
        cleaned_data = super().clean()
        email_address = cleaned_data.get('email_address')
        if not email_address:
            raise forms.ValidationError('Email address is required')
        return cleaned_data

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) > 1000:
            raise forms.ValidationError('Text should not exceed 1000 words')
        return message

    class Meta:
        """
        The meta class determines the fields accessible to the user
        """
        model = Contact
        fields = ['name', 'email_address', 'message', ]
