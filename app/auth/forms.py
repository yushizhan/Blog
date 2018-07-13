from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9]*$', 0, 'Only support letters, numbers')])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password', message='password must be eual')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9]*$', 0, 'Only support letters, numbers')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
