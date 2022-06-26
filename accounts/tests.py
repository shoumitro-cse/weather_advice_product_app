from django.urls import reverse
from rest_framework.test import APITestCase
import ast
from accounts.models import User


class TokenTests(APITestCase):
    def test_get_jwt_token(self):
        user = User.objects.create_superuser("admin@gmail.com", "1111")
        response = self.client.post(
            reverse('token_obtain_pair_api'),
            {'email': user.email, "password": '1111'},
            format='json'
        )
        dict_str = response.content.decode("UTF-8")
        token = ast.literal_eval(dict_str)
        print(repr(token.get("access")))
        print(repr(token.get("refresh")))
        assert response.status_code == 200
