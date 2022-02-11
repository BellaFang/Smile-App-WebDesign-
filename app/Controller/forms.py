from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, PasswordField
from wtforms.validators import  ValidationError, DataRequired, Length, Email, EqualTo 
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput 
from app.Model.models import Tag, User
from wtforms.fields.core import BooleanField

def gettag():
     return Tag.query.all()
     
def getname(theTag):
     return theTag.name
# Flask-WTF forms for "creating a post" and "sorting all posts". 

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Post', validators=[DataRequired(), Length(min=1, max=1500)])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])
    tag =  QuerySelectMultipleField( 'Tag', query_factory=gettag , get_label=getname, widget=ListWidget(prefix_label=False),
    option_widget=CheckboxInput() )
    submit = SubmitField('Post')

class SortForm(FlaskForm):
     sort_by= SelectField('Choice for users', choices =[(1,'Date'),(2,'Title'),(3,'# of likes'),(4,'Happiness_level')])
     checkbox=BooleanField('Display my posts only')
     submit = SubmitField('Refresh')

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('Password')])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Sign in')

class EmptyForm(FlaskForm):
   submit = SubmitField('Submit')