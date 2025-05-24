from flask import Flask
from flask_caching import Cache
from flasgger import Swagger
from flask_httpauth import HTTPBasicAuth

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize extensions
cache = Cache(app)
auth = HTTPBasicAuth()

# Configure Swagger
swagger = Swagger(app)

# Import utilities (after 'auth' is defined)
from utils import auth as auth_utils

# Import routes (after 'app' is fully initialized)
from route import auth, scrape
