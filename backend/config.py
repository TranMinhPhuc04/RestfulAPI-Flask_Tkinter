import os

class Config:
    # Sử dụng tên dịch vụ 'database' từ docker-compose.yml thay vì '127.0.0.1'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@database:5432/student_db1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
