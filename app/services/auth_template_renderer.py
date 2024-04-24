from flask import render_template

class AuthTemplateRenderer:
    def __init__(self):
        pass

    def render_login(self, form):
        return render_template(
            'login.html',
            form=form
        )
    
    def render_register(self, form):
        return render_template(
            'register.html',
            form=form
        )