from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    The UserProfile model class defines all the fields in the class.
    It creates a table in the database which stores each objects data.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    profile_image = CloudinaryField('image', default='placeholder')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def user_image(self):
        return self.image

    class Meta:
        """
        The UserProfile model Meta class.
        Each instance is ordered by creation date.
        """
        ordering = ['create_at']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    The create_profile function triggers a signal
    everytime a new user is created.
    It will associate this user to a
    profile which is also created at that time.
    It will then populate the profile with the user,
    username and email fields,
    from the newly created user.
    """
    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )


@receiver(post_save, sender=UserProfile)
def edit_profile(sender, instance, created, **kwargs):
    """
    The edit_profile function triggers a signal
    everytime a user is altered.
    It will associate this user to their profile in the database.
    It will then alter and save the fields in the
    user and profile objects,
    based on the user input.
    """
    user_profile = instance
    user = user_profile.user

    if created is False:
        user.first_name = user_profile.name
        user.username = user_profile.username
        user.email = user_profile.email
        user.save()


class Contact(models.Model):
    """
    The Contact model class defines all the fields in the class.
    It creates a table in the database which stores each objects data.
    """
    name = models.CharField(max_length=50)
    email_address = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
