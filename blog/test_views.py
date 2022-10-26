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

    def test_get_edit_blog_post_page(self):
        item = Post.objects.create(
            title='Masala milk',
            author=User.objects.create(),
            featured_image='',
            excerpt='Milk prepared with spices',
            meal_type=2,
            food_type=3,
            content='Some content'
        )
        response = self.client.reverse('edit_post/10')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')
