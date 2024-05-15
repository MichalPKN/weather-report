import app.services.weather_service as WeatherService
from flask import request

class ApiProcessor:
    def __init__(self):
        self.weather_service = WeatherService.WeatherService()
    
    def json_weather(self):
        city = request.args.get('city')
        if not city:
            city = 'Prague'
        return self.weather_service.get_weather(city)
    
    def json_weather_premium(self):
        city = request.args.get('city')
        if not city:
            city = 'Prague'
        return self.weather_service.get_premium_weather(city)