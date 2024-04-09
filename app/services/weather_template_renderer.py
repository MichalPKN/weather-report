from flask import render_template

class WeatherTemplateRenderer:
    def __init__(self):
        pass

    def render_weather(self, weather_data):
        return render_template(
            'current_weather.html',
            city=weather_data['location']['name'],
            icon=weather_data['current']['condition']['icon'],
            temperature=weather_data['current']['temp_c'],
        )