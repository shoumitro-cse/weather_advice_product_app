from rest_framework.permissions import IsAuthenticated
from weather.models import WeatherType
from weather.serializer import WeatherTypeSerializer


class BaseWeatherTypViewMixin:
    serializer_class = WeatherTypeSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = WeatherType.objects.all()