from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import ModelForm
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_summernote.widgets import SummernoteWidget


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
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
    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )


@receiver(post_save, sender=UserProfile)
def edit_profile(sender, instance, created, **kwargs):
    user_profile = instance
    user = user_profile.user

    if created is False:
        user.first_name = user_profile.name
        user.username = user_profile.username
        user.email = user_profile.email
        user.save()


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


