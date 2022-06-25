from rest_framework.permissions import IsAuthenticated
from products.models import ProductType
from products.serializer import ProductTypeSerializer
from base import mixin


class ProductTypeListCreateView(mixin.ListCreateAPIView):
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

    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = ProductType.objects.all()


class ProductTypeUpdateDeleteDestroyView(mixin.RetrieveUpdateDestroyAPIView):
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

    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = ProductType.objects.all()
