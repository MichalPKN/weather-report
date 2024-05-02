from flask import Blueprint, redirect, url_for
import app.services.weather_processor as WeatherProcessor
from flask_login import current_user

weather_controller = Blueprint('weather_controller', __name__)
weather_processor = WeatherProcessor.WeatherProcessor()

@weather_controller.route('/')
def show_weather():
    if current_user.is_authenticated:
        return weather_processor.process_premium_weather(current_user.id)
    return weather_processor.process_weather()

@weather_controller.route('/add_to_fav')
def add_to_fav():
    if current_user.is_authenticated:
        city = weather_processor.add_city_to_fav(current_user.id)
        return redirect(url_for('weather_controller.show_weather', city=city))
    return "user is logged out"