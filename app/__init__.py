from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# Initialize extensions
mongo = PyMongo()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Set Flask configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')

    # Initialize extensions with the app
    mongo.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
