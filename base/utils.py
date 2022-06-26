import requests
from django.conf import settings


def get_temperature(lat, lon):
    temperature_data = {}
    try:
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.WEATHER_API_KEY}")
        temperature_data["temp"] = req.json()['main']['temp']
        temperature_data["min_temp"] = req.json()["main"]["temp_min"]
        temperature_data["max_temp"] = req.json()["main"]["temp_max"]
    except Exception as e:
        print(e)
    return temperature_data
