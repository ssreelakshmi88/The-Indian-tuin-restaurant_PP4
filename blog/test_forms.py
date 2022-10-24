from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):

    def test_form_data_input_is_valid(self):
        form = PostForm(data={
            'title': 'Quinoa Dosa',
            'featured_image': '',
            'excerpt': 'An Indian dish',
            'meal_type': 1,
            'food_type': 3,
            'content': 'Some content'
        })

        self.assertTrue(form.is_valid())
  
    def test_title_field_cannot_be_empty(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_content_field_cannot_be_empty(self):
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(
            form.Meta.fields,
            (  
                'title',
                'featured_image',
                'excerpt',
                'meal_type',
                'food_type',
                'content'
             )
        )


class TestCommentForm(TestCase):
    """
    A class for testing the Comment form.
    """

    def test_form_data_input_is_valid(self):
        form = CommentForm(data={
            'email': 'lakshmi@email.com',
            'body': 'some comment',
        })

        self.assertTrue(form.is_valid())

    def test_body_field_cannot_be_empty(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields,
            ('body', )
        )

