from flask import Blueprint, redirect, url_for
from flask_login import login_user, login_required, logout_user
import app.services.auth_template_renderer as AuthTemplateRenderer
import app.services.auth_processor as AuthProcessor
from app.models.auth_form import RegisterForm, LoginForm

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        AuthProcessor.AuthProcessor().register_user(form)
        return redirect(url_for('auth_controller.login'))
    return AuthTemplateRenderer.AuthTemplateRenderer().render_register(form)

@auth_controller.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = AuthProcessor.AuthProcessor().login_user(form)
        if user:
            login_user(user)
            return redirect('/')
        else:
            form.password.errors.append('Incorrect credentials')
    return AuthTemplateRenderer.AuthTemplateRenderer().render_login(form)

@auth_controller.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_controller.login'))