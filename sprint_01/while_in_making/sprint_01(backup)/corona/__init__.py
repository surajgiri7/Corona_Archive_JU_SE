from flask import Flask
from crypt import methods
from enum import unique
from flask_sqlalchemy import SQLAlchemy #for SQLite database
from flask_bcrypt import Bcrypt #we will use flask_bcrypt algorithm or module to hash the passwords
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '6e34cf794b88973456e861d627adae4b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///corona.db' #creates a db file in the same directory as the app.py

#databse instance
db = SQLAlchemy(app)

#inititalizing the bcrypt instance for hashing password
bcrypt = Bcrypt(app)

#creating the instance for the login manager.
login_manager = LoginManager(app)

from corona import routes


