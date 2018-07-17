#encoding=utf8

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms import ValidationError
from ..models import *

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9]*$', 0, 'Only support letters, numbers')])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password', message='password must be eual')])
    submit = SubmitField('Register')

    # Handle all validate in Forms    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9]*$', 0, 'Only support letters, numbers')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
