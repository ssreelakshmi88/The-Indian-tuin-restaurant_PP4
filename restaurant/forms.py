from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Reservation


class DateInput(forms.DateInput):
    """
    This class defines to select date with the help of datepicker
    """
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    """
    This defines the user form output for the
    Reservation model class
    """

    class Meta:
        """
        Meta class defines the associated models and
        the fields accessible to the user.
        """
        model = Reservation
        fields = [
            'name',
            'email',
            'number_of_persons',
            'date',
            'time'
        ]
        widgets = {
            'date': DateInput(),
        }

    # Disable the past dates in date input widget
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date', 'min': timezone.localdate().strftime('%Y-%m-%d')
        }))

    def clean_email(self):
        """
        Validates the email field
        """
        email = self.cleaned_data['email']
        if email.endswith('@example.com'):
            raise ValidationError('Invalid email address')
        return email

    def clean_name(self):
        """
        Validates the name field
        """
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise ValidationError('Invalid name')
        return name
