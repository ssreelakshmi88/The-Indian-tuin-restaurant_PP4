from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import PostForm
import datetime as date


class TestBlogModels(TestCase):
    """
    This class tests the blog models.
    """
    def test_done_post_list_done_now(self):
        item = Post.objects.create(
            title='Masala milk',
            author=User.objects.create(),
            excerpt='Milk with spices',
            meal_type=2,
            food_type=4,
            content='Some content'
        )
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())
