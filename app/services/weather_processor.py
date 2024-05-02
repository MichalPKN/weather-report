import app.services.weather_service as WeatherService
import app.services.weather_template_renderer as WeatherTemplateRenderer
import app.services.fav_cities_service as FavCitiesService
from flask import request

class WeatherProcessor:
    def __init__(self):
        self.weather_service = WeatherService.WeatherService()
        self.weather_template_renderer = WeatherTemplateRenderer.WeatherTemplateRenderer()
        self.fav_cities_service = FavCitiesService.FavCitiesService()

    def process_weather(self):
        city = request.args.get('city')
        if not city:
            city = 'Prague'
        weather_data = self.weather_service.get_weather(city)
        rendered_page = self.weather_template_renderer.render_weather(weather_data)
        return rendered_page
    
    def process_premium_weather(self, name):
        city = request.args.get('city')
        if not city:
            city = 'Prague'
        weather_data = self.weather_service.get_premium_weather(city)
        cities = self.fav_cities_service.get_fav_cities(name)
        rendered_page = self.weather_template_renderer.render_premium_weather(weather_data, cities)
        return rendered_page
    
    def add_city_to_fav(self, name):
        city = request.args.get('city')
        self.fav_cities_service.add_fav_city(name, city)
        return city