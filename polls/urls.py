"""
URL configuration for the polls app.

This module defines all the URL patterns used in the polls application,
including question views, voting logic, blog-style posts, and user authentication.

Each URL is connected to a specific view in the `polls.views` module or includes external routes.
"""

from django.urls import path, re_path, include
from . import views

#: App namespace for URL reversing (e.g., {% url 'polls:detail' question.id %})
app_name = 'polls'

#: URL patterns for the polls application
urlpatterns = [
    # Homepage of the polls app – shows the latest questions
    path('', views.index, name='index'),

    # Detail view for a specific question by its ID
    path('<int:question_id>/', views.detail, name='detail'),

    # Results page for a specific question by its ID
    path('<int:question_id>/results/', views.results, name='results'),

    # Handles voting logic for a specific question by its ID
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # Example blog post URL using regex:
    # Matches URLs like /blog/2025/07/some-post-title/
    re_path(
        r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$',
        views.detail,
        name='blog_detail'
    ),

    # Includes Django's built-in authentication views (e.g., login, logout, password management)
    path('user_auth/', include("django.contrib.auth.urls")),

    # Includes custom authentication app URLs (e.g., signup, profile)
    path('user_auth/', include("user_auth.urls")),
]
