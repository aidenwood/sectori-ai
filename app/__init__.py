from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Load the configuration file
app.config.from_object('config')

# Import the views module (i.e., routes.py) to register the routes
from app import routes
