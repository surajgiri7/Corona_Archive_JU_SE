import email
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from corona.models import Visitor, Place, Hospital

# creating the registration forms for the Visitor 
# to store the data into the database
class visitorRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    visitor_name = StringField('Name', validators=[DataRequired()])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    device_id = StringField('Device ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # creating custom validation to check if the provided username is already in the data base
    def validate_username(self, username):
        visitor = Visitor.query.filter_by(username=username.data).first()
        if visitor:
            raise ValidationError('Username Already Taken.')
    
    # creating custom validation to check if the provided email is already in the data base
    def validate_email(self, email):
        visitor = Visitor.query.filter_by(email=email.data).first()
        if visitor:
            raise ValidationError('Email Already Taken.')
# to be edited


# creating the registration forms for the Place 
# to store the data into the database
class placeRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    place_name = StringField('Name', validators=[DataRequired()])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # creating custom validation to check if the provided username is already in the data base
    def validate_username(self, username):
        place = Place.query.filter_by(username=username.data).first()
        if place:
            raise ValidationError('Username Already Taken.')

    # creating custom validation to check if the provided email is already in the data base
    def validate_email(self, email):
        place = Place.query.filter_by(email=email.data).first()
        if place:
            raise ValidationError('Email Already Taken.')


# creating the registration forms for the hospital 
# to store the data into the database
class hospitalRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    hospital_name = StringField('Name', validators=[DataRequired()])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Add Hospital')

    # creating custom validation to check if the provided username is already in the data base
    def validate_username(self, username):
        hospital = Hospital.query.filter_by(username=username.data).first()
        if hospital:
            raise ValidationError('Username Already Taken.')

    # creating custom validation to check if the provided email is already in the data base
    def validate_email(self, email):
        hospital = Hospital.query.filter_by(email=email.data).first()
        if hospital:
            raise ValidationError('Email Already Taken.')


# creating the login form for the Visitor to login 
# everything that is shown in the empty visitor login form is coded here
class visitorLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# creating the login form for the Place to login 
# everything that is shown in the empty Place login form is coded here
class placeLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# creating the login form for the Hospital to login 
# everything that is shown in the empty Hospital login form is coded here
class hospitalLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# creating the login form for the Agent to login 
# everything that is shown in the empty Agent login form is coded here
class agentLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')