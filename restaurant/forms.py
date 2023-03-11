from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Reservation
from django.forms import TextInput
from django.core.validators import EmailValidator


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
            'name': forms.TextInput(
                attrs={
                    'required': True,
                    "class": "form-control",
                    "pattern": "[A-Za-z ]+",
                    "title": "Name can only contain letters",
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'required': True,
                    "class": "form-control",
                    "pattern": '[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,}$',
                    "title": "Please enter a valid email address",
                }
            ),
                  }

    # Disable the past dates in date input widget
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date', 'min': timezone.localdate().strftime('%Y-%m-%d')
        }))

    def clean(self):
        """
        Validates the date and time fields to ensure
        a user is not allowed to book a reservation
        for today after the current time.
        """
        cleaned_data = super().clean()
        chosen_date = cleaned_data.get("date")
        chosen_time = cleaned_data.get("time")
        if chosen_date == timezone.now().date() and chosen_time:
            current_hour = timezone.now().hour
            earliest_hour = {
                1: 11,
                2: 12,
                3: 13,
                4: 14,
                5: 16,
                6: 18,
                7: 20,
            }.get(chosen_time)
            if current_hour >= earliest_hour:
                raise forms.ValidationError(
                    "Reservation cannot be booked today after current time."
                    )
        return cleaned_data
