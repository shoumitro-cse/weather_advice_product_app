from django.urls import path
from weather.views import (
    WeatherTypeListCreateView,
    WeatherTypeUpdateDeleteDestroyView,
)

urlpatterns = [
    #  This URL is used for weather create or to see weather lists
    path('weather/', WeatherTypeListCreateView.as_view(), name='weather_create_list'),
    # This URL is used for weather retrieve, partially or fully update and delete
    path('weather/<int:pk>/', WeatherTypeUpdateDeleteDestroyView.as_view(),
         name='weather_retrieve_update_delete'),
]