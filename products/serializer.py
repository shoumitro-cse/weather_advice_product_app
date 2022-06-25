from products.models import Product, ProductType
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('vendor', 'is_active', 'created_at', 'created_by', 'updated_at', 'updated_by',)


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        exclude = ('is_active', 'created_at', 'created_by', 'updated_at', 'updated_by', )
