import app.services.weather_service as WeatherService
from flask import request

class WeatherProcesser:
    def __init__(self):
        self.weather_service = WeatherService.WeatherService()

    def process_weather(self):
        city = request.args.get('city')
        if not city:
            city = 'Prague'
        weather_data = self.weather_service.get_weather(city)
        return weather_data