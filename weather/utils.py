import requests
from django.conf import settings
from .models import WeatherData
from django.utils import timezone
from datetime import timedelta
from django.db.models import Avg


def fetch_weather_data(city):
    url = f"{settings.OPENWEATHER_BASE_URL}?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('cod') == 200:  # Check if API call was successful
            weather_data = WeatherData(
                city=city,
                temperature=data['main']['temp'],
                humidity=data['main']['humidity'],
                wind_speed=data['wind']['speed'],
                condition=data['weather'][0]['description']
            )
            weather_data.save()
            return weather_data, None
        else:
            error_message = data.get('message', 'Data not found.')
            return None, error_message
    else:
        return None, 'Failed to retrieve weather data. Please try again later.'


def calculate_weather_trends(city):
    last_24_hours = timezone.now() - timedelta(hours=24)
    weather_records = WeatherData.objects.filter(city=city, timestamp__gte=last_24_hours)

    if weather_records.exists():
        avg_temperature = weather_records.aggregate(Avg('temperature'))['temperature__avg']
        avg_humidity = weather_records.aggregate(Avg('humidity'))['humidity__avg']
        wind_speed = weather_records.latest('timestamp').wind_speed
        latest_condition = weather_records.latest('timestamp').condition

        return {
            'avg_temperature': avg_temperature,
            'avg_humidity': avg_humidity,
            'wind_speed': wind_speed,
            'latest_condition': latest_condition
        }
    return None


def check_extreme_weather(weather_data):
    extreme_conditions = ['storm', 'tornado', 'hurricane', 'snow', 'thunderstorm']
    if weather_data.temperature < -10 or weather_data.temperature > 40:
        return 'Extreme temperature detected!'

    if any(cond in weather_data.condition.lower() for cond in extreme_conditions):
        return 'Extreme weather condition detected!'

    return None
