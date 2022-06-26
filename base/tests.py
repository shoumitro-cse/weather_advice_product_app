import ast
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from accounts.models import User
from base.constants import VENDOR, CUSTOMER


class BaseAPITestCase(APITestCase):

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        return {
            "access": token.access_token,
        }

    def get_token_from_url(self, user, password):
        response = self.client.post(path=reverse('token_obtain_pair_api'),
                                    data={
                                        'email': user.email,
                                        "password": password
                                    }, format='json')
        dict_str = response.content.decode("UTF-8")
        return ast.literal_eval(dict_str)

    def get_token_from_admin_user(self):
        return self.get_token_from_url(User.objects.create_superuser("admin@gmail.com", "1111"), "1111")

    def get_token_from_vendor_user(self):
        vendor = User.objects.create_user("vendor@gmail.com", "2222", VENDOR)
        data = self.get_token_from_url(vendor, "2222")
        data.update({"vendor": vendor})
        return data

    def get_token_from_customer_user(self):
        return self.get_token_from_url(User.objects.create_user("customer@gmail.com", "2222", CUSTOMER), "3333")
