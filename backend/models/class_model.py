from . import db


class Class(db.Model):
    __tablename__ = 'class'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)

    # Define a one-to-many relationship with Student
    students = db.relationship('Student', back_populates='class_', lazy=True)
