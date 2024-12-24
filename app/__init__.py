from flask import Flask
from flask_pymongo import PyMongo
from config import Config

# Flask app initialize karna
app = Flask(__name__)

# MongoDB URI set karna
# app.config["MONGO_URI"] = "mongodb://localhost:27017/app"

# Load configuration
app.config.from_object(Config)  # Load from Config class
mongo = PyMongo(app)




# Routes import karenge
from app.routes import *
