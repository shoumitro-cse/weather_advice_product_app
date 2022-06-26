import ast
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase


class BaseAPITestCase(APITestCase):

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        return {
            "access": token.access_token,
        }

    def get_token_from_url(self, user):
        response = self.client.post(
            reverse('token_obtain_pair_api'),
            {'email': user.email, "password": '1111'},
            format='json'
        )
        dict_str = response.content.decode("UTF-8")
        return ast.literal_eval(dict_str)