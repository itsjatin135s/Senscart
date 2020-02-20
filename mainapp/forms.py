from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mainapp.models import User
from mainapp.__init__ import db
from flask_sqlalchemy import SQLAlchemy


class RegistrationFrom(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')


    def validate_username(self,username):
        
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken please choose a different one ')

    
    def validate_email(self,email):
        
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email I.D already registered')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

    
        
