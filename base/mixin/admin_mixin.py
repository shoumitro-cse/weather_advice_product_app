from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView as BaseRetrieveUpdateDestroyAPIView,
    ListCreateAPIView as BaseListCreateAPIView
)
from rest_framework import status
from rest_framework.response import Response
from base.mixin.user_mixin import AdminMixin


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
