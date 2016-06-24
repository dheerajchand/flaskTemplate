# ------------------------------------------------------------------------
# views.py - Here we declare our API endpoints and any custom decorators
#
# Authors: Jonathan Kramer
# 
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#       Import modules
# ------------------------------------------------------------------------
from flask_sqlalchemy import SQLAlchemy

from app import app

# ------------------------------------------------------------------------
#       Connect to our database
# ------------------------------------------------------------------------

db = SQLAlchemy(app)

# ------------------------------------------------------------------------
#       Model Definitions
# ------------------------------------------------------------------------

# example of Flask-SQLAlchemy User model
# class User(db.Model):
#     # id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255), index=True, unique=True)
#     name = db.Column(db.String(255), index=True, unique=True)
    
#     password = db.Column(db.String(255))
#     loginToken = db.Column(db.String(64))
#     passwordResetToken = db.Column(db.String(64))

#     lastLogin = db.Column(db.DateTime)
#     loginTokenExpires = db.Column(db.DateTime)

#     following = db.Column(db.JSONB)
#     settings = db.Column(db.JSONB)

class User(db.Model):
    __tablename__ = 'poops'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
    
    def to_json(self):
        return "{'id' : '%d', 'username' : '%s', 'email' : '%s'}" % (self.id, self.username, self.email)

