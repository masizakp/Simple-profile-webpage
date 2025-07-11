"""
URL configuration for the user_auth app.

This module defines URL patterns for handling user authentication,
including login, registration, and user dashboard views.

Each URL is mapped to a corresponding view function in user_auth.views.
"""

from django.urls import path
from user_auth import views

#: App namespace for template URL resolution (e.g., {% url 'user_auth:login' %})
app_name = 'user_auth'

#: URL patterns for the authentication system
urlpatterns = [
    path(
        '', 
        views.user_login, 
        name='login'
    ),
    path(
        'authenticate_user/', 
        views.authenticate_user, 
        name='authenticate_user'
    ),
    path(
        'user/', 
        views.show_user, 
        name='show_user'
    ),
    path(
        'register/', 
        views.register, 
        name='register'
    ),
]
