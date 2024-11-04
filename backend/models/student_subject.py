from . import db


class StudentSubject(db.Model):
    __tablename__ = 'student_subject'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)  # ID tự động tăng
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student_register.id', ondelete="CASCADE"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey(
        'subject.id'), nullable=False)
    semester = db.Column(db.String(10))  # Ví dụ: "2023-1" (học kỳ 1 năm 2023)
    year = db.Column(db.Integer)         # Năm học, ví dụ: 2023
    grade = db.Column(db.Float)          # Điểm số của sinh viên trong môn học

    # Thiết lập quan hệ đến Student và Subject
    student = db.relationship('Student', back_populates='subjects')
    subject = db.relationship('Subject', back_populates='students')
