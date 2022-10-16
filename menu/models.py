from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Menu(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True
        )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


