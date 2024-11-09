from . import db


class Student(db.Model):
    __tablename__ = 'student_register'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.Date)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=True)

    # Many-to-many relationship with Subject through StudentSubject
    subjects = db.relationship(
        "StudentSubject", back_populates="student", cascade="all, delete-orphan")

    # Set up a one-to-many relationship with Class
    class_ = db.relationship(
        "Class", back_populates="students", overlaps="class_")
