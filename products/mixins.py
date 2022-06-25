from rest_framework.permissions import IsAuthenticated
from products.models import ProductType, Product
from products.serializer import (
    ProductTypeSerializer, ProductSerializer
)


class BaseProductViewMixin:
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Product.objects.all()


class BaseProductTypeViewMixin:

    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = ProductType.objects.all()
