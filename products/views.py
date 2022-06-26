from django.db.models import Q
from django.template.defaultfilters import title

from base.mixin import admin_mixin
from base.mixin import vendor_mixin
from products.mixins import BaseProductViewMixin, BaseProductTypeViewMixin
from rest_framework import generics
from rest_framework.permissions import AllowAny


class ProductListCreateView(BaseProductViewMixin, vendor_mixin.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create product or to see all products.
    Only Authenticated vendor users will be able to perform it.
    when a vendor user try to send this request:
    <ul>
        <li> It performs create operation after sending a post request </li>
        <li> It gives a list of product after sending a get request.</li>
    </ul>
    </div>
    """
    pass


class ProductUpdateDeleteDestroyView(BaseProductViewMixin, vendor_mixin.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for product crud operation.
    it is only for Authenticated vendor users. <br/>Non-Authenticated users
    or simple users can't access it. when a vendor user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the product details after sending a get request.</li>
    </ul>
    </div>
    """
    pass


class ProductTypeListCreateView(BaseProductTypeViewMixin, admin_mixin.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create product type like normal, hot, cold
    or to see all product types. Only Authenticated admin super will be able to see it.
    when an admin user try to send this request:
    <ul>
        <li> It performs create operation after sending a post request </li>
        <li> It gives a list of product after sending a get request.</li>
    </ul>
    </div>
    """
    pass


class ProductTypeUpdateDeleteDestroyView(BaseProductTypeViewMixin, admin_mixin.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for product type crud operation.
    it is only for Authenticated admin users. <br/>Non-Authenticated users
    or simple users can't access it. when an admin user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the product type details after sending a get request.</li>
    </ul>
    </div>
    """
    pass


class CustomerProductView(BaseProductViewMixin, generics.ListAPIView):
    """
    <div style='text-align: justify;'>
    Using this API,  customers will be able to see all the products and
    also will be able to search for products using the product's name or weather type.
    <ul>
        <li> By default, It will see all products if someone sends only get request </li>
        <li> If someone sends a get request with a filter query,  only filtered products will be seen.</li>
    </ul>

    <pre>
    Filter products using the product's name or weather type.
    Here,
    protocol = http, https
    port = 80, 800 etc
    domain = localhost or others
    {protocol}://{domain}:{port}/api/customer/product/?product_name={Your product name}&weather_type={Weather like hot, cold}
    </pre>
    </div>
    """
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        query = Q()
        if self.request.GET.get("product_name", None):
            query |= Q(title__icontains=self.request.GET.get("product_name", None))
        if self.request.GET.get("weather_type", None):
            query |= Q(weather_type__name__icontains=self.request.GET.get("weather_type", None))
        return self.model.objects.filter(query)
