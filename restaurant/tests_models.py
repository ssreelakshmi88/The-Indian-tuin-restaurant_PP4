from django.test import TestCase
from .models import Reservation, Photo
import datetime as date


class TestBlogModels(TestCase):
    """
    This class tests the models in restaurant class.
    """
    def test_done_reservation_list_done_now(self):
        item = Reservation.objects.create(
           email='lakshmi@email.com',
           number_of_persons=3,
           date='2022-08-22',
           time=3,
        )
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())
