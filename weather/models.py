from django.db import models
from base import BaseModel


CELSIUS = 'C'
FAHRENHEIT = 'F'


TEMPERATURE_TYPE_CHOICES = (
    (CELSIUS, 'CELSIUS'),
    (FAHRENHEIT, 'FAHRENHEIT'),
)


class WeatherType(BaseModel):
    name = models.CharField(max_length=50)
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    temp_type = models.CharField(max_length=1, choices=TEMPERATURE_TYPE_CHOICES,
                                 default=FAHRENHEIT)

    class Meta:
        verbose_name = "Weather Type"
        verbose_name_plural = "Weather Types"

