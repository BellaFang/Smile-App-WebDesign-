from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Email
from app.Model.models import User

# Flask-WTF forms for authentication use cases, i.e., "registering a new user" and "login". 
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username): 
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The username already exists! Please use a different username.')

    def validate_email(self,email): 
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email already exists! Please use a different email address.')

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Sign in')