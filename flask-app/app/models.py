# ------------------------------------------------------------------------
# views.py - Here we declare our API endpoints and any custom decorators
#
# Authors: Jonathan Kramer
# 
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#       Import modules
# ------------------------------------------------------------------------

from app import db

# ------------------------------------------------------------------------
#       Model Definitions
# ------------------------------------------------------------------------

# example of Flask-SQLAlchemy User model
class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), index=True, unique=True)
    name = db.Column(db.String(255), index=True, unique=True)
    
    password = db.Column(db.String(255))
    loginToken = db.Column(db.String(64))
    passwordResetToken = db.Column(db.String(64))

    lastLogin = db.Column(db.DateTime)
    loginTokenExpires = db.Column(db.DateTime)

    following = db.Column(db.JSONB)
    settings = db.Column(db.JSONB)

