from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, InputRequired, ValidationError
import json
import sys

class RegisterForm(FlaskForm): 
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=25)]) 
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        Length(max=50, message='Password must be less than 50 characters long'),
        Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[A-Za-z\\d@$!%*?&]+$', 
               message='Password must have at least one lowercase letter, one uppercase letter and one number')
        ])
    confirm_password = PasswordField('Confirm Password', validators=[
        EqualTo('password', message='Passwords must match'),
        DataRequired()
        ])
    submit = SubmitField('Submit')
    def validate_name(form, field):
        with open('app/data/users.json', 'r') as f:
            users = f.read()
            if not users:
                return
            print("\n\n brooo \n\n", users, file=sys.stderr)
            users = json.loads(users)
            #print(users, file=sys.stderr)
            if field.data in [user['name'] for user in users]:
                raise ValidationError('Username already exists')

class LoginForm(FlaskForm): 
    name = StringField('Name', validators=[InputRequired(), Length(min=4, max=25)]) 
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50)])
    submit = SubmitField('Submit')