from django.shortcuts import render
from .utils import fetch_weather_data, calculate_weather_trends, check_extreme_weather
from .forms import CityForm

def weather_view(request):
    """
    Depending on the request method, this view performs the following actions:
    - On GET requests, it displays a form for users to input a city name.
    - On POST requests, it processes the form submission, fetches weather data
      for the specified city, calculates weather trends, and checks for extreme
      weather conditions.

    Args:
        request (HttpRequest): The HTTP request object, which contains data about
        the request, including any form data submitted by the user.

    Returns:
        HttpResponse: The rendered HTML page with the weather information, form,
        and any error messages or alerts.

    Endpoint:
        - Local Setup: http://127.0.0.1:8000/weather
        - Deployed Endpoint: [Provide the deployed endpoint URL here]
    """
    form = CityForm()
    weather_data = None
    weather_trends = None
    extreme_alert = None
    error_message = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data, error_message = fetch_weather_data(city)
            if weather_data:
                weather_trends = calculate_weather_trends(city)
                extreme_alert = check_extreme_weather(weather_data) if weather_data else None

    context = {
        'form': form,
        'weather_data': weather_data,
        'weather_trends': weather_trends,
        'extreme_alert': extreme_alert,
        'error_message': error_message,
    }

    return render(request, 'weather_info.html', context)
