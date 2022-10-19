from django import forms
from django.forms import ModelForm
from .models import Reservation
from .widgets import FengyuanChenDatePickerInput


class ReservationForm(ModelForm):
    """
    This defines the user form output for the
    Reservation model class
    """
    date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=FengyuanChenDatePickerInput()
        )

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
