from django.db import models
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    """
    Creates a table in the database which stores photos"
    """
    title = models.CharField(max_length=150)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
