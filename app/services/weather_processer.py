import app.services.weather_service as WeatherService
import app.services.weather_template_renderer as WeatherTemplateRenderer
from flask import request

class WeatherProcesser:
    def __init__(self):
        self.weather_service = WeatherService.WeatherService()
        self.weather_template_renderer = WeatherTemplateRenderer.WeatherTemplateRenderer()

    def process_weather(self):
        city = request.args.get('city')
        if not city.strip():
            city = 'Prague'
        weather_data = self.weather_service.get_weather(city)
        rendered_page = self.weather_template_renderer.render_weather(weather_data)
        return rendered_page