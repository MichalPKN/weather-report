from flask import Blueprint
import app.services.auth_template_renderer as AuthTemplateRenderer

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/register')
def register():
    return AuthTemplateRenderer.AuthTemplateRenderer().render_register()

@auth_controller.route('/login')
def login():
    return AuthTemplateRenderer.AuthTemplateRenderer().render_login()