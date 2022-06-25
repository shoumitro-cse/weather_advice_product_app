from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from accounts.models import User, Profile
from accounts.serializer import UserSerializer, UserProfileSerializer


class UserListCreateView(generics.ListCreateAPIView):
    """ This class is to be used to register and to see all users.
    Only Authenticated admin super will be able to see it"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()

    def list(self, *args, **kwargs):
        message = "Non-Authenticated users can't access it."
        if self.request.user.is_authenticated:
            if self.request.user.user_type == User.ADMIN and self.request.user.is_superuser:
                return super().list(*args, **kwargs)
            message = "The user must be an admin to get all user data."
        return Response({"error": message}, status.HTTP_400_BAD_REQUEST)


class UserUpdateDeleteDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """  This class is used to get for four http methods functionality like
        get, put, patch, delete for crud operation. it is only for
        Authenticated users. Non-Authenticated users can't access it."""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()

