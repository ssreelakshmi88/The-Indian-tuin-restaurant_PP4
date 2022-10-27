from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This model class defines all the fields in the class.
    Creates a table in the database which stores each objects data.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    meal_type = models.PositiveSmallIntegerField(choices=(
        (1, 'starter'),
        (2, 'main'),
        (3, 'dessert'),
    ), null=True)
    food_type = models.PositiveSmallIntegerField(choices=(
        (1, 'rice'),
        (2, 'bread and rotis'),
        (3, 'meat'),
        (4, 'fish'),
        (5, 'drinks'),
        (6, 'sweet'),
        (7, 'seafood'),
        (8, 'vegetarian'),
        ), null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
    The Post model meta class defines the occurence of instances.
    It also defines the string representation of the post class.
    """
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    The Comment model class defines all the fields in the class.
    It creates a table in the database which stores each objects data.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
    The Comment model meta class defines the occurence of instances.
    It also defines the string representation of the Comment class.
    """

    ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
