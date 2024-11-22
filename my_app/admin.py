from django.contrib import admin

from my_app.models import CartItem, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
