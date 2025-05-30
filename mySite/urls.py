"""
URL configuration for mySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from personal import views
#from eShopping import views

'''from personal.views import(home_screen_view,)
from personal.views import(products_view,)


urlpatterns = [
    path("admin/", admin.site.urls),    
    path('', include('personal.urls')), 
    
]
from django.urls import path
from personal import views  # Adjust if the view is in a different app'''

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_screen_view, name="home"),
   # path("products/", views.product_list_view, name="products"),
    path("eShopping/", views.eshopping, name="eShopping"),  # <-- Add this line
]

