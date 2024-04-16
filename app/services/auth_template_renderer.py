from flask import render_template

class AuthTemplateRenderer:
    def __init__(self):
        pass

    def render_login(self):
        return render_template(
            'login.html'
        )
    
    def render_register(self):
        return render_template(
            'register.html'
        )