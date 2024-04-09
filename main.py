from flask import Flask
from app.controllers.weather_controller import weather_controller
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

app = Flask(__name__, template_folder='app/templates') #maybe to config.py
app.static_folder = 'app/static'

app.register_blueprint(weather_controller)


if __name__ == '__main__':
    app.run(debug=True)
