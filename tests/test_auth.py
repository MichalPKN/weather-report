import pytest
#import os, sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from main import User
from app.models.auth_form import LoginForm, RegisterForm
from app.services.auth_processor import AuthProcessor
import json
from flask_login import UserMixin, login_user

class User(UserMixin):
    pass

def test_login_and_logout(client):
    #login
    login_response = client.post('/login', data=dict(
        name='asdasd',
        password='asdASD123'
    ), follow_redirects=True)
    assert b'class="link">Logout</a>' in login_response.data
    #logout
    response = client.get('/logout', follow_redirects=True)
    assert b'class="link">Login</a>' in response.data

def test_wrong_login(client):
    response = client.post('/login', data=dict(
        name='wronguser',
        password='wrongpassword'
    ))
    assert b'Incorrect credentials' in response.data

def test_register(client):
    user = {
        'name': 'newuser',
        'password': 'newPASS123',
        'fav_cities': []
    }
    #register
    response = client.post('/register', data=dict(
        name=user['name'],
        password=user['password'],
        confirm_password=user['password']
    ), follow_redirects=True)
    assert b'<div class="form-title">Login</div>' in response.data
    #try to register an existing user
    response = client.post('/register', data=dict(
        name=user['name'],
        password=user['password'],
        confirm_password=user['password']
    ), follow_redirects=True)
    assert b'Username already exists' in response.data
    #delete the registered user
    with open('app/data/users.json', 'r+') as f:
        users = json.load(f)
        print(users)
        assert user in users
        users.remove(user)
        f.seek(0)
        f.truncate()
        f.write(json.dumps(users))