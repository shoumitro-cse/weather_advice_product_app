from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from accounts.models import User, Profile
from accounts.serializer import UserSerializer, UserProfileSerializer


class UserListCreateView(generics.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to register like john, justin etc person account
    or to see all user lists. register api also open for Non-Authenticated user
    and Only Authenticated admin super will be able to see user lists.<br/>
    when an admin user try to send this request:
    <ul>
        <li> It performs register operation after sending a post request </li>
        <li> It gives a list of user after sending a get request.</li>
    </ul>
    </div>
    """

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
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for user crud operation.
    it is only for Authenticated users. <br/>Non-Authenticated users can't access it.
    when an admin user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the user details after sending a get request.</li>
    </ul>
    </div>
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()


class UserProfileCreateView(generics.CreateAPIView):
    """
    <div style='text-align: justify;'>
    It is used to create the profile of an authenticated user.
    when an user try to send this request:
    <ul>
        <li> It performs create operation after sending a post request </li>
    </ul>
    </div>
    """

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
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for user crud operation.
    it is only for Authenticated users. Non-Authenticated users can't access it.
    when an user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the user profile details after sending a get request.</li>
    </ul>
    </div>
    """

    def get_object(self):
        return self.request.user.profile if hasattr(self.request.user, "profile") \
            else Profile.objects.create(user=self.request.user)

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]

