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


class Reservation(models.Model):
    """
    Reservation model class.
    Creates a table in the database which stores each objects data"
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    number_of_persons = models.PositiveSmallIntegerField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ), null=True)
    date = models.DateField()
    time = models.PositiveSmallIntegerField(choices=(
        (1, '11:00-12:00'),
        (2, '12:00-13:00'),
        (3, '13:00-14:00'),
        (4, '14:00-15:00'),
        (5, '16:00-17:00'),
        (6, '18:00-19:00'),
        (7, '20:00-21:00'),
    ), null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + " " + str(self.date)

    class Meta:
        """
        The Reservation model Meta class.
        Defines that each instance is ordered by earliest date.
        """
        ordering = ['-date']
