import requests
import os
import sys

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = 'http://api.weatherapi.com/v1/'

    def get_weather(self, city):
        url = f'{self.base_url}current.json?q={city}&key={self.api_key}'
        try:
            response = requests.get(url, timeout=10)
            print(response.status_code, file=sys.stderr)
            weather = response.json()
            weather['status_code'] = response.status_code
            return weather
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}