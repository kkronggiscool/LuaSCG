# routes/routes.py
from flask import Blueprint, render_template

# Create a Blueprint for organizing routes
main = Blueprint('main', __name__)

# Main route for the index page
@main.route('/')
def index():
    return render_template('index.html')
