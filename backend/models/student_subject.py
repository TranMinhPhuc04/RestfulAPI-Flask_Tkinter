from . import db


class StudentSubject(db.Model):
    __tablename__ = 'student_subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student_register.id', ondelete="CASCADE"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey(
        'subject.id'), nullable=False)
    # Example: "2023-1" (1st semester of 2023)
    semester = db.Column(db.String(10))
    year = db.Column(db.Integer)         # Academic year, e.g., 2023
    grade = db.Column(db.Float)          # Student's grade in the subject

    # Relationship setup to Student and Subject
    student = db.relationship('Student', back_populates='subjects')
    subject = db.relationship('Subject', back_populates='students')
