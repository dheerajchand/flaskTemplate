import os
import urlparse
import json
from flask import Flask, jsonify

# from flask_cors import CORS, cross_origin
# from config import basedir

app = Flask(__name__)
app.config.from_object('config')

# # FOR psycopg2 USAGE 
# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ.get("DATABASE_URL"))
# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

# # FOR CORS SETUP
# CORS(app)

@app.errorhandler(404)
def page_not_found(e):
	return jsonify(error=404, text=str(e)), 404

@app.after_request
def apply_access_control_header(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Authorization'
	return response

import views
