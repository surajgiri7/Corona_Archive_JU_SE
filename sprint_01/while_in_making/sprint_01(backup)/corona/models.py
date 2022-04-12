from flask import session
from corona import db, login_manager
from datetime import datetime
from flask_login import UserMixin

#for loading visitor for login from the db
@login_manager.user_loader
def load_user(user_id):
        if session['user'] == "Visitor":
            return Visitor.query.get(int(user_id))  
        elif session['user'] == "Place":
            return Place.query.get(int(user_id))
        elif session['user'] == "Hospital":
            return Hospital.query.get(int(user_id))
        elif session['user'] == "Agent":
            return Agent.query.get(int(user_id))
        else:
            return None

class Visitor(db.Model, UserMixin):
    citizen_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    visitor_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150),unique=True, nullable=False)
    device_id = db.Column(db.String(50),unique=True, nullable=False)
    infected = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"Visitor('{self.citizen_id}', '{self.username}', '{self.visitor_name}', '{self.address}', '{self.city}', '{self.email}', '{self.infected}' )"
    
    def get_id(self):
        return self.citizen_id

class Place(db.Model, UserMixin):
    place_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    place_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150),unique=True, nullable=False)
    QRCode = db.Column(db.String(100), nullable=False, default='Request QRCode')

    def __repr__(self):
        return f"Place('{self.place_id}', '{self.username}', '{self.place_name}', '{self.address}', '{self.city}', '{self.email}', '{self.QRCode}')"

    def get_id(self):
        return self.place_id

class Hospital(db.Model, UserMixin):
    hospital_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    hospital_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150),unique=True, nullable=False)

    def __repr__(self):
        return f"Hospital('{self.hospital_id}', '{self.username}', '{self.hospital_name}', '{self.address}', '{self.city}', '{self.email}')"

    def get_id(self):
        return self.hospital_id

class Agent(db.Model, UserMixin):
    agent_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Agent('{self.agent_id}', '{self.username}')"

    def get_id(self):
        return self.agent_id

#Create the relationship#
# class VisitorToPlaces(db.Model):
#     QRCode = db.Column(db.String(100), db.ForeignKey("Place.QRCode"))
#     device_ID = db.Column(db.String(50), db.ForeignKey("Visitor.device_id"))
#     entry_date = db.Column(db.Date, primary_key = True, default=datetime.utcnow)
#     entry_time = db.Column(db.String(128), primary_key = True)
#     exit_date = db.Column(db.Date, nullable=False)
#     exit_time = db.Column(db.String(128), nullable=False)

#     def __repr__(self):
#         return f"VisitorToPlaces('{self.QRCode}', '{self.entry_date}', '{self.entry_time}', '{self.exit_date}', '{self.exit_time}')"
