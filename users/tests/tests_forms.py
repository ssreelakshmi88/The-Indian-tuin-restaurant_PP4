from django.test import TestCase
from .forms import UserProfileForm, ContactForm


class TestUserProfileForm(TestCase):
    """
    This class tests the user profile form
    """
    def test_form_data_input_is_valid(self):
        form = UserProfileForm(data={
         'name': 'Lakshmi',
         'username': 'Lakshmi1234',
         'email': 'lakshmi@gmail.com'

        })
        self.assertTrue(form.is_valid())

    def test_user_can_be_empty(self):
        form = UserProfileForm({'user': ''})
        self.assertTrue(form.is_valid())

    def test_username_can_be_empty(self):
        form = UserProfileForm({'username': ''})
        self.assertTrue(form.is_valid())

    def test_email_can_be_empty(self):
        form = UserProfileForm({'email': ''})
        self.assertTrue(form.is_valid())
