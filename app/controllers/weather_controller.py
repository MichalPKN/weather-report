from flask import Blueprint, redirect, url_for
import app.services.weather_processor as WeatherProcessor
import app.services.api_processor as ApiProcessor
from flask_login import current_user

weather_controller = Blueprint('weather_controller', __name__)

@weather_controller.route('/')
def show_weather():
    weather_processor = WeatherProcessor.WeatherProcessor()
    if current_user.is_authenticated:
        return weather_processor.process_premium_weather(current_user.id)
    return weather_processor.process_weather()

@weather_controller.route('/add_to_fav')
def add_to_fav():
    if current_user.is_authenticated:
        weather_processor = WeatherProcessor.WeatherProcessor()
        city = weather_processor.add_city_to_fav(current_user.id)
        return redirect(url_for('weather_controller.show_weather', city=city))
    return "error - user is logged out"

@weather_controller.route('/remove_from_fav')
def remove_from_fav():
    if current_user.is_authenticated:
        weather_processor = WeatherProcessor.WeatherProcessor()
        city = weather_processor.remove_city_from_fav(current_user.id)
        return redirect(url_for('weather_controller.show_weather', city=city))
    return "error - user is logged out"

@weather_controller.route('/api')
def rest_api():
    api_processor = ApiProcessor.ApiProcessor()
    if current_user.is_authenticated:
        return api_processor.json_weather_premium()
    return api_processor.json_weather()