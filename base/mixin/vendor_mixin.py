from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView as BaseRetrieveUpdateDestroyAPIView,
    ListCreateAPIView as BaseListCreateAPIView
)
from rest_framework import status
from rest_framework.response import Response
from base.mixin.user_mixin import UserMixin
from products.models import Product


class ListCreateAPIView(UserMixin, BaseListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    error_message = "User must be vendor."

    def get_queryset(self):
        return Product.objects.filter(vendor=self.get_user())

    def get(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(vendor=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveUpdateDestroyAPIView(UserMixin, BaseRetrieveUpdateDestroyAPIView):
    """
    This class only for admin user.
    Concrete view for retrieving, updating or deleting a model instance.
    """

    def get(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().delete(request, *args, **kwargs)
