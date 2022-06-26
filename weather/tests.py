from django.urls import reverse
from base.tests import BaseAPITestCase
from rest_framework import status
from weather.models import WeatherType


class WeatherTypeTests(BaseAPITestCase):

    """
    To run this test case:
    python manage.py test weather.tests.WeatherTypeTests
    """

    def test_get_weather_type_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        response = self.client.get(path=reverse('weather_create_list'))
        assert response.status_code == status.HTTP_200_OK

    def test_create_weather_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        weather_type_data = {
            "name": "hot",
            "temp_min": 100,
            "temp_max": 200,
            "temp_type": "F"
        }
        response = self.client.post(path=reverse('weather_create_list'),
                                    data=weather_type_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_weather_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        weather_type = WeatherType.objects.create(name="cold", temp_min=1, temp_max=20, temp_type="C")
        weather_type_data = {
            "name": "hot",
            "temp_min": 100,
            "temp_max": 200,
            "temp_type": "F"
        }
        response = self.client.put(path=reverse('weather_retrieve_update_delete', kwargs={'pk': weather_type.id}),
                                    data=weather_type_data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_weather_temp_range_update(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        weather_type = WeatherType.objects.create(name="cold", temp_min=5, temp_max=30, temp_type="C")
        weather_type_data = {
            "temp_min": 140,
            "temp_max": 190
        }
        response = self.client.patch(path=reverse('weather_retrieve_update_delete', kwargs={'pk': weather_type.id}),
                                     data=weather_type_data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_weather_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        weather_type = WeatherType.objects.create(name="cold", temp_min=5, temp_max=30, temp_type="C")
        response = self.client.get(path=reverse('weather_retrieve_update_delete', kwargs={'pk': weather_type.id}))
        assert response.status_code == status.HTTP_200_OK

    def test_delete_weather_type(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token_from_admin_user().get("access")}')
        weather_type = WeatherType.objects.create(name="cold", temp_min=5, temp_max=30, temp_type="C")
        response = self.client.delete(path=reverse('weather_retrieve_update_delete', kwargs={'pk': weather_type.id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT

