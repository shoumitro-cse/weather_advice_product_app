from django.urls import path
from accounts.views import (
    UserUpdateDeleteDestroyView,
    UserListCreateView
)

urlpatterns = [
    #  This URL is used for user registration and to see user lists
    path('user/', UserListCreateView.as_view(), name='register'),
    # This URL is used for a user to retrieve, partially or fully update and delete
    path('user/<int:pk>/', UserUpdateDeleteDestroyView.as_view(),
         name='user_retrieve_update_delete'),
]