from django.urls import reverse
from base.tests import BaseAPITestCase
from rest_framework import status
from products.models import ProductType


class ProductTypeTests(BaseAPITestCase):

    """
    To run this test case:
    python manage.py test products.tests.product_type_tests.ProductTypeTests
    """

    def test_get_product_type_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        response = self.client.get(path=reverse('product_type_create_list'))
        assert response.status_code == status.HTTP_200_OK

    def test_create_product_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        product_type_data = {
            "name": "hot",
        }
        response = self.client.post(path=reverse('product_type_create_list'),
                                    data=product_type_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_product_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        product_type = ProductType.objects.create(name="cold")
        product_type_data = {
            "name": "hot",
        }
        response = self.client.put(path=reverse('product_type_retrieve_update_delete', kwargs={'pk': product_type.id}),
                                    data=product_type_data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_update_product_type_partially(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        product_type = ProductType.objects.create(name="cold")
        product_type_data = {
            "name": "hot",
        }
        response = self.client.patch(path=reverse('product_type_retrieve_update_delete', kwargs={'pk': product_type.id}),
                                     data=product_type_data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_product_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        product_type = ProductType.objects.create(name="cold")
        response = self.client.get(path=reverse('product_type_retrieve_update_delete', kwargs={'pk': product_type.id}))
        assert response.status_code == status.HTTP_200_OK

    def test_delete_product_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        product_type = ProductType.objects.create(name="cold")
        response = self.client.delete(path=reverse('product_type_retrieve_update_delete', kwargs={'pk': product_type.id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT

