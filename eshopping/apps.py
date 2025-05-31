"""
App configuration for the eshopping Django app.

This module defines the configuration settings for the eshopping application,
including the default primary key field type and the app name used by Django.
"""

from django.apps import AppConfig

class EshoppingConfig(AppConfig):
    """
    Configuration class for the eshopping application.

    Sets the default auto-generated primary key field type to BigAutoField
    and registers the app name as 'eshopping'.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "eshopping"
