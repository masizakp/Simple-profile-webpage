from django.urls import path, re_path, include
from . import views

app_name = 'polls'

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

    # Includes Django's built-in authentication views (e.g., login, logout)
    path('user_auth/', include("django.contrib.auth.urls")),

    # Includes custom authentication app URLs (e.g., signup, profile)
    path('user_auth/', include("user_auth.urls")),
]
