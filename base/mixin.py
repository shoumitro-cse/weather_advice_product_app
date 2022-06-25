from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView as BaseRetrieveUpdateDestroyAPIView,
    ListCreateAPIView as BaseListCreateAPIView
)
from rest_framework import status
from rest_framework.response import Response
from accounts.models import User


class AdminMixin:
    error_message = {"error": "The user must be an admin."}

    def is_admin_user(self, *args, **kwargs):
        return self.request.user.user_type == User.ADMIN and self.request.user.is_superuser


class ListCreateAPIView(AdminMixin, BaseListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        if not self.is_admin_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.is_admin_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(AdminMixin, BaseRetrieveUpdateDestroyAPIView):
    """
    This class only for admin user.
    Concrete view for retrieving, updating or deleting a model instance.
    """

    def get(self, request, *args, **kwargs):
        if not self.is_admin_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not self.is_admin_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if not self.is_admin_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not self.is_admin_user():
            return Response(self.error_message, status.HTTP_400_BAD_REQUEST)
        return super().delete(request, *args, **kwargs)
