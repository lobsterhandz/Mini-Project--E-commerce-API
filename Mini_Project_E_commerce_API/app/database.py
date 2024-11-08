# database.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Create Flask app instance
app = Flask(__name__)

# Configure database connection
# Using environment variables for security; falls back to SQLite if not provided
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy and Flask-Migrate
# SQLAlchemy is used for ORM, and Flask-Migrate is used to handle database migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Example model import statement to avoid circular imports (models should be imported after db is initialized)
# from app.models import *

# Notes:
# - Environment variables should be used to securely provide sensitive information like DATABASE_URL.
# - To run migrations, use the following commands:
#   flask db init      -> Initializes a new migrations directory
#   flask db migrate   -> Creates a new migration script based on model changes
#   flask db upgrade   -> Applies the migrations to the database
