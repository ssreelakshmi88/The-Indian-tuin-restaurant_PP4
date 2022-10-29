from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    UsersConfig defines contact field, user profile field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
