import datetime as date
from django.test import TestCase
from .models import Menu, Category


class TestBlogModels(TestCase):
    """
    This class tests the models in menu class.
    """
    def test_done_menu_list_done_now(self):
        item = Menu.objects.create(
           name='Tandoori chicken',
           description='Delicious and spicy chicken',
           price=9.99,
        )
        self.assertTrue(item)

    def test_done_category_list_done_now(self):
        item = Category.objects.create(
           name='Lunch',
        )
        self.assertTrue(item)
