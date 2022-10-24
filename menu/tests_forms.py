from django.test import TestCase
from .forms import MenuForm


class TestMenuForm(TestCase):
    """
    This class tests the Menu form.
    """

    def test_form_data_input_is_valid(self):
        form = MenuForm(data={
            'name': 'Tandoori Chicken',
            'description': 'Grilled Chicken',
            'category': 'lunch',
            'price': 9.99,
            'featured_image': '',
        })
     
        self.assertFalse(form.is_valid())

    def test_name_field_cannot_be_empty(self):
        form = MenuForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_description_field_cannot_be_empty(self):
        form = MenuForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_category_field_cannot_be_empty(self):
        form = MenuForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0],
                         'This field is required.')

    def test_price_field_cannot_be_empty(self):
        form = MenuForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MenuForm()
        self.assertEqual(
            form.Meta.fields,
            '__all__'
        )