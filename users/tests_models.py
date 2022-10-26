from django.test import TestCase
from .models import UserProfile
import datetime as date


class TestBlogModels(TestCase):
    """
    This class tests the models in user class.
    """
    def test_done_user_profile_done_now(self):
        item = UserProfile.objects.create()
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.create_at.date())