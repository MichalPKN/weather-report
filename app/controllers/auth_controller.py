from flask import Blueprint
import app.services.auth_template_renderer as AuthTemplateRenderer
import app.services.auth_processor as AuthProcessor
from app.models.auth_form import RegisterForm, LoginForm

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        AuthProcessor.AuthProcessor().register_user(form)
    return AuthTemplateRenderer.AuthTemplateRenderer().render_register(form)

@auth_controller.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return AuthTemplateRenderer.AuthTemplateRenderer().render_login(form)