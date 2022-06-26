from django.db import models
from base.models import BaseModel
from weather.models import WeatherType
from accounts.models import User


class ProductType(BaseModel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"


class Product(BaseModel):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/product/', null=True, blank=True)
    product_type = models.ForeignKey(ProductType, related_name='products',
                                     on_delete=models.SET_NULL, null=True, blank=True)
    weather_type = models.ForeignKey(WeatherType, related_name='products',
                                     on_delete=models.SET_NULL, null=True, blank=True)
    vendor = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
