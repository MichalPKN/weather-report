import pytest
import requests

def login_user(client):
    client.post('/login', data=dict(
        name='asdasd',
        password='asdASD123'
    ), follow_redirects=True)

def test_default_city(client):
    response = client.get("/")
    assert b'<h2 class="city">Prague</h2>' in response.data

def test_Liberec(client):
    response = client.get("/?city=Liberec")
    assert b'<h2 class="city">Liberec</h2>' in response.data

def test_city_not_found(client):
    response = client.get("/?city=NonExistingCity")
    assert b'<h2 class="city">Something went wrong</h2>' in response.data
    assert b'<p>No matching location found.</p>' in response.data

def test_premium_weather(client):
    login_user(client)
    response = client.get("/")
    assert b'<div class="weather-day">' in response.data
    assert b'<h2 class="city">Prague</h2>' in response.data

def test_premium_weather_wrong_city(client):
    login_user(client)
    response = client.get("/?city=NonExistingCity")
    assert b'<h2 class="city">Something went wrong</h2>' in response.data
    assert b'<p>No matching location found.</p>' in response.data

def test_fav_city(client):
    login_user(client)
    #adding city to fav
    response = client.get("/add_to_fav?city=Liberec", follow_redirects=True)
    assert b'<a class="city-link" href="/?city=Liberec">Liberec</a>' in response.data
    assert b'<h2 class="city">Liberec</h2>' in response.data
    #trying to add the same city again
    response = client.get("/add_to_fav?city=Liberec", follow_redirects=True)
    assert b'<a class="city-link" href="/?city=Liberec">Liberec</a>' in response.data
    assert b'<h2 class="city">Liberec</h2>' in response.data
    #removing city from fav
    response = client.get("/remove_from_fav?city=Praha,Liberec", follow_redirects=True)
    assert b'<a class="city-link" href="/?city=Liberec">Liberec</a>' not in response.data
    assert b'<h2 class="city">Praha</h2>' in response.data

def test_api(client):
    response = client.get("/api")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json['location']['name'] == 'Prague'
    assert 'current' in response.json
    assert 'temp_c' in response.json['current']
    assert 'icon' in response.json['current']['condition']
    assert 'localtime' in response.json['location']

def test_api_city(client):
    response = client.get("/api?city=Liberec")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json['location']['name'] == 'Liberec'

def test_api_premium(client):
    login_user(client)
    response = client.get("/api")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json[0]['location']['name'] == 'Prague'
    assert len(response.json) == 5
    assert 'avgtemp_c' in response.json[0]['forecast']['forecastday'][0]['day']
    assert 'icon' in response.json[0]['forecast']['forecastday'][0]['day']['condition']
    assert 'date' in response.json[0]['forecast']['forecastday'][0]