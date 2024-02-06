from flask import Blueprint

# Create a Blueprint for your routes
api_blueprint = Blueprint('api', __name__)

from . import prediction_routes, health_check_routes
