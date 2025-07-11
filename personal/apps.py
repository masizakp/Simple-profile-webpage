"""
App configuration for the personal app.

This module defines application-level settings used by Django
to register and initialize the personal app.
"""

from django.apps import AppConfig


class PersonalConfig(AppConfig):
    """
    Configuration class for the personal app.

    Sets the default auto field type and registers the app
    under the name 'personal'.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "personal"
