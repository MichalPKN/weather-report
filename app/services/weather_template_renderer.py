from flask import render_template

class WeatherTemplateRenderer:
    def __init__(self):
        pass

    def render_weather(self, weather_data):
        if self.check_error(weather_data):
            return self.check_error(weather_data)
        return render_template(
            'current_weather.html',
            city=weather_data['location']['name'],
            icon=weather_data['current']['condition']['icon'],
            temperature=weather_data['current']['temp_c'],
        )
    
    def render_premium_weather(self, weather_data):
        weather = []
        for day in weather_data:
            if self.check_error(day):
                return self.check_error(day)
            weather.append({
                'date': day['forecast']['forecastday'][0]['date'],
                'icon': day['forecast']['forecastday'][0]['day']['condition']['icon'],
                'temperature': day['forecast']['forecastday'][0]['day']['avgtemp_c'],
            })
        return render_template(
            'premium_weather.html',
            city=weather_data[0]['location']['name'],
            weather=weather,
        )
    
    def check_error(self, weather_data):
        if weather_data['status_code'] != 200:
            return render_template(
                'current_weather_error.html',
                error_message=weather_data['error']['message'],
            )
        return None