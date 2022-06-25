from weather.models import WeatherType
from rest_framework import serializers


class WeatherTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherType
        exclude = ('is_active', 'created_at', 'created_by', 'updated_at', 'updated_by', )
