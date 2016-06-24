import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
SECRET_KEY = 'my precious'

PG_DB_NAME = 'postgres'
PG_USER = 'postgres'
PG_PASSWORD = ''
PG_HOST = os.environ.get('PG_PORT_5432_TCP_ADDR')
PG_PORT = os.environ.get('PG_PORT_5432_TCP_PORT')

SQLALCHEMY_DATABASE_URI = 'postgresql://' + PG_USER + PG_PASSWORD + '@' + PG_HOST + ':' + PG_PORT + '/' + PG_DB_NAME
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Connect to the database
# SQLALCHEMY_DATABASE_URI = 'postgresql://' + os.path.join(basedir, 'database.db')

# etc