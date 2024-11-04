from flask_sqlalchemy import SQLAlchemy

# Khởi tạo SQLAlchemy instance
db = SQLAlchemy()

# Import các model để sử dụng khi khởi động ứng dụng
from .student_register import Student
from .class_model import Class
from .subject import Subject
from .student_subject import StudentSubject