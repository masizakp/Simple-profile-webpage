from django.apps import AppConfig

class UserAuthConfig(AppConfig):
    """
    Configuration class for the user_auth Django application.

    This class defines application-specific settings such as the default
    primary key field type and the name used to reference the app in the
    Django project.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_auth"
