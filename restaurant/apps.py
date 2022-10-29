from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    """
    This is an app consisting of reservation fields
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'
