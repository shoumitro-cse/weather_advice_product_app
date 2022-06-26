from django.urls import reverse
from base.tests import BaseAPITestCase
from rest_framework import status
from accounts.models import User


class TokenTests(BaseAPITestCase):
    """
    To run this test case:
    python manage.py test accounts.tests.token_tests.TokenTests
    """

    def test_get_jwt_token(self):
        user = User.objects.create_superuser("admin@gmail.com", "1111")
        response = self.client.post(path=reverse('token_obtain_pair_api'),
                                    data={'email': user.email, "password": '1111'},
                                    format='json')
        assert response.status_code == status.HTTP_200_OK
