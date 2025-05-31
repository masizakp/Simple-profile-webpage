"""
URL configuration for the Django project.

This module maps URL paths to corresponding view functions.
Currently, it routes:
- the root URL ('') to the home_screen_view in the personal app
- the 'admin/' URL to the Django admin site
"""

from django.contrib import admin
from django.urls import path
from personal import views  # Import views from the personal app

# Define URL patterns to map paths to views
urlpatterns = [
    # Route for the Django admin interface
    path("admin/", admin.site.urls),

    # Route for the home page
    path("", views.home_screen_view, name="home"),
]
