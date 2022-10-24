from .models import Menu
from django import forms
from django.forms import ModelForm


class MenuForm(ModelForm):
    """
    The MenuForm class defines the user form output for the Menu model class.
    """
    class Meta:
        """
        The Meta class defines which model is associated and from that model,
        which fields will be accessible to the user.
        """
        model = Menu
        fields = '__all__'
