from django.urls import reverse
from base.tests import BaseAPITestCase
from rest_framework import status
from products.tests.product_tests import ProductBaseCase


class CustomersTests(ProductBaseCase, BaseAPITestCase):

    """
    To run this test case:
    python manage.py test products.tests.customer_tests.CustomersTests
    """

    def test_get_product_list_for_customer(self):
        self.create_product(self.create_vendor("rahim"))
        product_name = "hot temp dress"
        weather_type = "cold"
        lat = 90
        lon = 24
        response = self.client.get(path=reverse('customer_product')\
                                        +f"?product_name={product_name}&weather_type={weather_type}")

        data = '[{"id":1,"title":"hot temp dress","price":"122.50",' \
               '"quantity":13,"image":null,"product_type":1,"weather_type":1}]'
        assert response.status_code == status.HTTP_200_OK
        assert response.content == bytes(data, 'utf-8')
        response = self.client.get(path=reverse('customer_product')+f"?lat={lat}&lon={lon}")
        assert response.status_code == status.HTTP_200_OK
        assert response.content == bytes(data, 'utf-8')
