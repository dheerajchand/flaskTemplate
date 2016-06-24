import os
import urlparse
import json
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS, cross_origin

# from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)

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
	
	@property
	def json(self):
		return to_json(self, self.__class__)


# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ.get("DATABASE_URL"))
# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

# # conn = psycopg2.connect("user='postgres' password='docker' host='localhost'")

# CORS(app)

@app.errorhandler(404)
def page_not_found(e):
	return jsonify(error=404, text=str(e)), 404

# @app.after_request
# def apply_access_control_header(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response

@app.after_request
def apply_access_control_header(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Authorization'
	return response

from app import views
