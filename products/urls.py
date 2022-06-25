from django.urls import path
from products.views import (
    ProductTypeListCreateView,
    ProductTypeUpdateDeleteDestroyView,
    ProductListCreateView,
    ProductUpdateDeleteDestroyView
)

urlpatterns = [
    #  This URL is used for product type create or to see product lists
    path('product/type/', ProductTypeListCreateView.as_view(),
         name='product_type_create_list'),
    # This URL is used for product type retrieve, partially or fully update and delete
    path('product/type/<int:pk>/', ProductTypeUpdateDeleteDestroyView.as_view(),
         name='product_type_retrieve_update_delete'),
    #  This URL is used for product create or to see product lists
    path('vendor/product/', ProductListCreateView.as_view(), name='product_create_list'),
    # This URL is used for product retrieve, partially or fully update and delete
    path('vendor/product/<int:pk>/', ProductUpdateDeleteDestroyView.as_view(),
         name='product_retrieve_update_delete'),
]