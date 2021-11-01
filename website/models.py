from . import db
from flask_login import UserMixin

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email =	db.Column(db.String(50))
    source = db.Column(db.String(30))
    model =	db.Column(db.String(30))
    phone =	db.Column(db.String(20))
    last = db.Column(db.String(20))
    stage =	db.Column(db.String(20))
    notes = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    leads = db.relationship('Lead')