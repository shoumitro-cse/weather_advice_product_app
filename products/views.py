from base.mixin import admin_mixin
from base.mixin import product_mixin
from products.mixins import ProductBaseViewMixin, ProductTypeBaseViewMixin


class ProductListCreateView(ProductBaseViewMixin, product_mixin.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create product or to see all products.
    Only Authenticated admin super will be able to perform it.
    when an admin user try to send this request:
    <ul>
        <li> It performs create operation after sending a post request </li>
        <li> It gives a list of product after sending a get request.</li>
    </ul>
    </div>
    """
    pass


class ProductUpdateDeleteDestroyView(ProductBaseViewMixin, product_mixin.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for product crud operation.
    it is only for Authenticated admin users. <br/>Non-Authenticated users
    or simple users can't access it. when an admin user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the product details after sending a get request.</li>
    </ul>
    </div>
    """
    pass


class ProductTypeListCreateView(ProductTypeBaseViewMixin, admin_mixin.ListCreateAPIView):
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


class ProductTypeUpdateDeleteDestroyView(ProductTypeBaseViewMixin, admin_mixin.RetrieveUpdateDestroyAPIView):
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
