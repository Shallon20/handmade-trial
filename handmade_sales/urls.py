"""
URL configuration for handmade_sales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('product/search', views.search_product, name='search_product'),
    path('products/details/<int:customer_id>', views.product_details, name='product_details'),
    path('add/product', views.add_product, name='add_product'),
    path('products/delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('products/update/<int:product_id>', views.update_product, name='update_product'),

    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('admin/', admin.site.urls),
]
