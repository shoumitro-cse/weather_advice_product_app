from django.urls import path
from products.views import (
    ProductTypeListCreateView,
    ProductTypeUpdateDeleteDestroyView,
)

urlpatterns = [
    #  This URL is used for weather create or to see weather lists
    path('product/type/', ProductTypeListCreateView.as_view(), name='product_create_list'),
    # This URL is used for weather retrieve, partially or fully update and delete
    path('product/type/<int:pk>/', ProductTypeUpdateDeleteDestroyView.as_view(),
         name='product_retrieve_update_delete'),
]