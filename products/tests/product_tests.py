from django.urls import reverse
from base.tests import BaseAPITestCase
from rest_framework import status
from products.models import Product, ProductType
from weather.models import WeatherType


class ProductBaseCase:

    def get_product_data(self):
        weather_type = WeatherType.objects.create(name="cold", temp_min=1, temp_max=20, temp_type="C")
        product_type = ProductType.objects.create(name="hot")
        return {
            "title": "hot temp dress",
            "price": 122.5,
            "quantity": 13,
            "product_type": product_type.id,
            "weather_type": weather_type.id,
        }

    def get_update_product_data(self):
        weather_type = WeatherType.objects.create(name="cold", temp_min=1, temp_max=20, temp_type="C")
        product_type = ProductType.objects.create(name="hot")
        return {
            "title": "hot temp dress",
            "price": 122.5,
            "quantity": 13,
            "product_type_id": product_type.id,
            "weather_type_id": weather_type.id,
        }


class ProductTests(ProductBaseCase, BaseAPITestCase):

    """
    To run this test case:
    python manage.py test products.tests.product_tests.ProductTests
    """

    def create_product(self, vendor):
        return Product.objects.create(vendor=vendor, **self.get_update_product_data())

    def test_get_product_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_vendor_user().get("access")}')
        response = self.client.get(path=reverse('product_create_list'))
        assert response.status_code == status.HTTP_200_OK

    def test_create_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_vendor_user().get("access")}')
        response = self.client.post(path=reverse('product_create_list'),
                                    data=self.get_product_data(), format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_product(self):
        data = self.get_token_from_vendor_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {data.get("access")}')
        product = self.create_product(data.get("vendor"))
        response = self.client.put(path=reverse('product_retrieve_update_delete', kwargs={'pk': product.id}),
                                   data=self.get_update_product_data(), format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_update_product_partially(self):
        data = self.get_token_from_vendor_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {data.get("access")}')
        product = self.create_product(data.get("vendor"))
        response = self.client.patch(path=reverse('product_retrieve_update_delete', kwargs={'pk': product.id}),
                                     data={"title": "cold temp dress",}, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_product(self):
        data = self.get_token_from_vendor_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {data.get("access")}')
        product = self.create_product(data.get("vendor"))
        response = self.client.get(path=reverse('product_retrieve_update_delete', kwargs={'pk': product.id}))
        assert response.status_code == status.HTTP_200_OK

    def test_delete_product(self):
        data = self.get_token_from_vendor_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {data.get("access")}')
        product = self.create_product(data.get("vendor"))
        response = self.client.delete(path=reverse('product_retrieve_update_delete', kwargs={'pk': product.id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT

