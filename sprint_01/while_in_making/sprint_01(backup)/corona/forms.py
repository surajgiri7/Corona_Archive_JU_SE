import email
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from corona.models import Visitor, Place, Hospital

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

    #checking if the respective data already exists in the data base.
    # i.e., creating custom validation
    def validate_username(self, username):
        visitor = Visitor.query.filter_by(username=username.data).first()
        if visitor:
            raise ValidationError('Username Already Taken.')

    def validate_email(self, email):
        visitor = Visitor.query.filter_by(email=email.data).first()
        if visitor:
            raise ValidationError('Email Already Taken.')
# to be edited

class placeRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    place_name = StringField('Name', validators=[DataRequired()])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #checking if the respective data already exists in the data base.
    # i.e., creating custom validation
    def validate_username(self, username):
        place = Place.query.filter_by(username=username.data).first()
        if place:
            raise ValidationError('Username Already Taken.')

    def validate_email(self, email):
        place = Place.query.filter_by(email=email.data).first()
        if place:
            raise ValidationError('Email Already Taken.')

class hospitalRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    hospital_name = StringField('Name', validators=[DataRequired()])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #checking if the respective data already exists in the data base.
    # i.e., creating custom validation
    def validate_username(self, username):
        hospital = Hospital.query.filter_by(username=username.data).first()
        if hospital:
            raise ValidationError('Username Already Taken.')

    def validate_email(self, email):
        hospital = Hospital.query.filter_by(email=email.data).first()
        if hospital:
            raise ValidationError('Email Already Taken.')

class visitorLoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class placeLoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class hospitalLoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class agentLoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')