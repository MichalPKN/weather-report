from flask import Blueprint
import app.services.weather_processor as WeatherProcessor
from flask_login import current_user

weather_controller = Blueprint('weather_controller', __name__)

@weather_controller.route('/')
def show_weather():
    weather_processor = WeatherProcessor.WeatherProcessor()
    if current_user.is_authenticated:
        return weather_processor.process_weather(True)
    return weather_processor.process_weather()