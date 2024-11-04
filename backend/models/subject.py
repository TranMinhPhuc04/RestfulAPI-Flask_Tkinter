from . import db

class Subject(db.Model):
    __tablename__ = 'subject'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # ID tự động tăng
    name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

    # Quan hệ nhiều-nhiều với Student thông qua StudentSubject
    students = db.relationship('StudentSubject', back_populates='subject')
