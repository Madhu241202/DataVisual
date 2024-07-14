import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '01514ed0c28175e79756aa5f55063f0559acc4927ee973e0')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/datavisual')
