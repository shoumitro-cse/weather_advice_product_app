from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView as BaseRetrieveUpdateDestroyAPIView,
    ListCreateAPIView as BaseListCreateAPIView
)
from rest_framework import status
from rest_framework.response import Response
from accounts.models import VENDOR


class VendorMixin:
    error_message = {"error": "The user must be an vendor."}

    def is_vendor_user(self, *args, **kwargs):
        return self.request.user.user_type == VENDOR and not self.request.user.is_superuser


class ListCreateAPIView(VendorMixin, BaseListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.is_vendor_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(VendorMixin, BaseRetrieveUpdateDestroyAPIView):
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
