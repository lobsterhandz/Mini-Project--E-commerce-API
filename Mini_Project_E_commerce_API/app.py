from flask import Flask
from app.database import db
from app.routes import customer_routes, customer_account_routes, product_routes, order_routes
from flask_migrate import Migrate
import os

# Create the Flask app
app = Flask(__name__)

# Configuration setup (using environment variables or fallback values)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Database and Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints for modular code structure
app.register_blueprint(customer_routes)
app.register_blueprint(customer_account_routes)
app.register_blueprint(product_routes)
app.register_blueprint(order_routes)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
