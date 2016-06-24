# ------------------------------------------------------------------------
# views.py - Here we declare our API endpoints and any custom decorators
#
# Authors: Jonathan Kramer
# 
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#       Import modules
# ------------------------------------------------------------------------

from flask import jsonify, request
from functools import wraps
import requests
import json

from app import app, User

# ------------------------------------------------------------------------
#       Decorator to easily protect API routes access
# ------------------------------------------------------------------------

def custom_decorator(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    # Decorator code goes here

    # if some condition
      # Return an error / something different 
    # else
    return f(*args, **kwargs)
  return decorated_function


# ------------------------------------------------------------------------
#       Routes
# ------------------------------------------------------------------------

@app.route('/', methods = ['GET'])
@custom_decorator
def home():
  print "Hit home!"
  users = User.query.all()
  print users
  return "Welcome to circavictor-flask, <strong>%s</strong>!" % users[0].username , 200

@app.route('/api/v1.0/example', methods = ['GET'])
@custom_decorator
def get_clients_route():
  return "API endpoint example", 200








