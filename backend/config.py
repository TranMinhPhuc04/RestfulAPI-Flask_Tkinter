import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1/student_db1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
