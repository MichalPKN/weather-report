from flask import Flask
from app.controllers.weather_controller import weather_controller

from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from app.controllers.auth_controller import auth_controller

app.template_folder = 'app/templates'
app.static_folder = 'app/static'

app.register_blueprint(weather_controller)
app.register_blueprint(auth_controller)

if __name__ == '__main__':
    app.run(debug=True)
