from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestBlogViews(TestCase):
    """
    This class tests blog app views.
    """
    def test_get_post_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

