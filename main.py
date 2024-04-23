from flask import Flask
from app.controllers.weather_controller import weather_controller
from flask_login import LoginManager, UserMixin

from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from app.controllers.auth_controller import auth_controller

app.template_folder = 'app/templates'
app.static_folder = 'app/static'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_controller.login'

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(user_id):
    user = User()
    user.id = user_id
    return user

app.register_blueprint(weather_controller)
app.register_blueprint(auth_controller)

if __name__ == '__main__':
    app.run(debug=True)
