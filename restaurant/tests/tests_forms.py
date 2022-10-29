from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):
    """
    This class tests the Reservation form
    """

    def test_form_data_input_is_valid(self):
        """
        This function tests the validity of input fields
        """

        form = ReservationForm(data={
            'name': 'lakshmi',
            'email': 'lakshmi@gmail.com',
            'number_of_persons': 3,
            'date': '06/21/2022',
            'time': 2,
        })

        self.assertTrue(form.is_valid())

    def test_time_field_cannot_be_empty(self):
        """
        This function ensures that the time field will not be empty
        """
        form = ReservationForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_date_field_cannot_be_empty(self):
        """
        This function ensures that the date field will not be empty
        """
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_email_field_cannot_be_empty(self):
        """
        This function ensures that the email field will not be empty
        """
        form = ReservationForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        This function ensures that the test fields are explicit
        """
        form = ReservationForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'name',
                'email',
                'number_of_persons',
                'date',
                'time'
            ]
        )
