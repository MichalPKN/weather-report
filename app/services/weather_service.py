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
        for day in range(2, 0, -1):
            day_date = (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d')
            weather = self.get_historical_date(city, day_date)
            days_weather.append(weather)
        days = 3
        forecast_url = f'{self.base_url}forecast.json?q={city}&days={days}&key={self.api_key}&aqi=no&alerts=no'
        try:
            response = requests.get(forecast_url, timeout=10)
            forecast = response.json()
            status_code = response.status_code
        except requests.exceptions.RequestException as e:
            return [{'error': {'message' : str(e)}, 'status_code': 500}]
        print("aaaaaaaaaaaaaa", len(forecast['forecast']['forecastday']), file=sys.stderr)
        for day in forecast['forecast']['forecastday']:
            day['status_code'] = status_code
            day['location'] = days_weather[0]['location']
            days_weather.append(day)
        print(days_weather, file=sys.stderr)
        return days_weather
            
    
    def get_historical_date(self, city, date):
        url = f'{self.base_url}history.json?q={city}&dt={date}&key={self.api_key}'
        try:
            response = requests.get(url, timeout=10)
            weather = response.json()
            weather['forecast']['forecastday'][0]['status_code'] = response.status_code
            weather['forecast']['forecastday'][0]['location'] = weather['location']['name']
            return weather['forecast']['forecastday'][0]
        except requests.exceptions.RequestException as e:
            return {'error': {'message' : str(e)}, 'status_code': 500}