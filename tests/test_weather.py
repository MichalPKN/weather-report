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