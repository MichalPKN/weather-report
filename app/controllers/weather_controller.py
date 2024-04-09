from flask import Blueprint
import app.services.weather_processer as WeatherProcesser

weather_controller = Blueprint('weather_controller', __name__)

@weather_controller.route('/')
def show_weather():
    weather_processer = WeatherProcesser.WeatherProcesser()
    return weather_processer.process_weather()