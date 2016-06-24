

# create user schema based on same one in Jefferson,

# create auth endpoints for login, signup, logout

# create decorator / middleware to put above api endpoints to protect them from non-users

from functools import wraps
from flask import request, redirect, url_for

# import the app and db connection
from app import db

# Decorator to easily protect API routes access
def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		# here we will deal with finding a user with proper token information based on the request

		# also be sure to check if our token has expired

		# if we found no users with matching token info, throw an error
		if :
			response = jsonify({'message': message})
    		response.status_code = 400
    		return response

		return f(*args, **kwargs)

	return decorated_function

#
# It may not be necessary for this backend to handle the actual assignment of tokens.
# Doesn't make sense to have to deal with all of the forget password logic and such here.
#

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	# check response data for email and password fields.
	# ensure they are safe and normalized

	# should we see if someone already exists here?
	
	# create a token for them using sha256

	# bcrypt password before storing 

	# set the token expiration

	# we may also have to set the lastLogin

@app.route('/login', methods=['GET', 'POST'])
def login():
	# check if they exist
	# check if they already have a token

	# create a token for them using sha256

	# update lastLogin and potentially token expiration

	# bcrypt password before storing 

@app.route('/logout', methods=['GET', 'POST'])
def logout():



