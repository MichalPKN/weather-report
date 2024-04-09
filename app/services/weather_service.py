import requests
import json
import os

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = 'http://api.weatherapi.com/v1/'

    def get_weather(self, city):
        url = f'{self.base_url}current.json?q={city}&key={self.api_key}'
        try:
            response = requests.get(url, timeout=10)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}