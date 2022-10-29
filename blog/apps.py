from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Blog Config app is for blog posts and comments
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
