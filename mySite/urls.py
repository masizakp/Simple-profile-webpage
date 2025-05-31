"""
URL configuration for the Django project.

This file defines the mapping between URL paths and the views that handle them.
Each path in the urlpatterns list routes a URL to a view function.
"""

from django.contrib import admin
from django.urls import path  # Required to define URL patterns

# Import views from the personal app
from personal import views as personal_views

# Import views from the eshopping app
from eshopping import views as shopping_views

# List of URL patterns to route incoming HTTP requests
urlpatterns = [
    # Admin site URL
    path("admin/", admin.site.urls),

    # Home page view (root URL)
    path("", personal_views.home_screen_view, name="home"),

    # eShopping page view
    path("eShopping/", shopping_views.eshopping, name="eShopping"),
]
