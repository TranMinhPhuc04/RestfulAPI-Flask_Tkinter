from . import db

class Class(db.Model):
    __tablename__ = 'class'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # ID tự động tăng
    name = db.Column(db.String(100), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)

    # Quan hệ một-nhiều với Student
    students = db.relationship('Student', backref='class', lazy=True)
