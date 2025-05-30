'''# personal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('products/', views.products_view, name='products'),
]'''

from django.contrib import admin
from django.urls import path
from personal import views  # Make sure this matches your actual app name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_screen_view, name="home"),
   # path("products/", views.product_list_view, name="products"),
    path("eShopping/", views.eshopping, name="eShopping"),  # optional, if added
]
