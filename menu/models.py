from django.db import models
from cloudinary.models import CloudinaryField

class Menu(models.model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(blank=True, null=True)
    food_type = models.PositiveIntegerField(choices=(
        (1, 'starter'),
        (2, 'main'),
        (3, 'dessert'),
    ), null=True)

    def __str__(self):
        return self.title
