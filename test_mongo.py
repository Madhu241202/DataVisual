from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
mongo_uri = os.getenv('MONGO_URI')

# Create a MongoDB client
client = MongoClient(mongo_uri)

# Try to list database names to ensure connection is successful
try:
    databases = client.list_database_names()
    print("Databases:", databases)
    print("Connection successful")
except Exception as e:
    print("Error connecting to MongoDB:", e)
