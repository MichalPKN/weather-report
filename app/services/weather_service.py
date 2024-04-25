import requests
import os
import sys
from datetime import datetime, timedelta

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = 'http://api.weatherapi.com/v1/'

    def get_weather(self, city):
        url = f'{self.base_url}current.json?q={city}&key={self.api_key}'
        try:
            response = requests.get(url, timeout=10)
            weather = response.json()
            weather['status_code'] = response.status_code
            return weather
        except requests.exceptions.RequestException as e:
            return {'error': {'message' : str(e)}, 'status_code': 500}
    
    def get_premium_weather(self, city):
        days_weather = []
        for day in range(4, -1, -1):
            day_date = (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d')
            weather = self.get_historical_date(city, day_date)
            days_weather.append(weather)
        return days_weather
            
    
    def get_historical_date(self, city, date):
        url = f'{self.base_url}history.json?q={city}&dt={date}&key={self.api_key}'
        try:
            response = requests.get(url, timeout=10)
            print(response.status_code, file=sys.stderr)
            weather = response.json()
            weather['status_code'] = response.status_code
            return weather
        except requests.exceptions.RequestException as e:
            return {'error': {'message' : str(e)}, 'status_code': 500}