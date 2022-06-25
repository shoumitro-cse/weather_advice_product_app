from django.contrib import admin
from products.models import Product, ProductType


admin.site.register(Product)
admin.site.register(ProductType)