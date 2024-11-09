from . import db


class Subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

    # Many-to-many relationship with Student through StudentSubject
    students = db.relationship('StudentSubject', back_populates='subject')
