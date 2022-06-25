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


class UserProfileCreateView(generics.CreateAPIView):
    """ It is used to create the profile of an authenticated user."""

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        if not hasattr(self.request.user, "profile"):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"error": "This user profile already exist."}, status.HTTP_400_BAD_REQUEST)


class UserProfileUpdateDeleteDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """  It is used to update the profile of an authenticated user."""

    def get_object(self):
        return self.request.user.profile if hasattr(self.request.user, "profile") \
            else Profile.objects.create(user=self.request.user)

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]

