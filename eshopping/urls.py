"""
URL configuration for the Django project (eshopping version).

This module maps URL paths to view functions.
It currently includes:
- the 'admin/' route for Django's admin interface
- the 'eshopping/' route for the eshopping page view
"""

from django.contrib import admin
from django.urls import path
from eshopping import views  # Import views from the eshopping app

# Define the URL patterns
urlpatterns = [
    # Route to Django's built-in admin panel
    path("admin/", admin.site.urls),

    # Route to the eshopping view
    path("eshopping/", views.eshopping, name="eshopping"),
]
