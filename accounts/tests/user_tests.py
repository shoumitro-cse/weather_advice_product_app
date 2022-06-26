from django.urls import reverse
from base.constants import CUSTOMER
from base.tests import BaseAPITestCase
from rest_framework import status
from accounts.models import User


class UsersTests(BaseAPITestCase):
    """
    To run this test case:
    python manage.py test accounts.tests.user_tests.UsersTests
    """

    def test_user_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        response = self.client.get(path=reverse('create_list'))
        assert response.status_code == status.HTTP_200_OK

    def test_register_user(self):
        data = {
          "first_name": "john",
          "last_name": "doe",
          "email": "john@gmail.com",
          "password": "1111",
          "user_type": CUSTOMER,
          "is_active": True
        }
        response = self.client.post(path=reverse('create_list'), data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_user(self):
        data = {
          "first_name": "justine",
          "last_name": "doe",
          "email": "justine@gmail.com",
          "password": "2232",
          "user_type": CUSTOMER,
          "is_active": True
        }
        user = User.objects.create_user("john@gmail.com", "1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_user(user, "1111").get("access")}')
        response = self.client.put(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}),
                                   data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_update_user_partially(self):
        data = {
          "first_name": "justine",
          "last_name": "doe",
        }
        user = User.objects.create_user("john@gmail.com", "1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_user(user, "1111").get("access")}')
        response = self.client.patch(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}),
                                   data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_user(self):
        user = User.objects.create_user("john@gmail.com", "1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_user(user, "1111").get("access")}')
        response = self.client.get(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}))
        assert response.status_code == status.HTTP_200_OK

    def test_delete_user(self):
        user = User.objects.create_user("john@gmail.com", "1111")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_user(user, "1111").get("access")}')
        response = self.client.delete(path=reverse('user_retrieve_update_delete', kwargs={'pk': user.id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT

