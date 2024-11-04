from flask import Blueprint, jsonify, request
from models import db
from models.student_subject import StudentSubject

enrollment_blueprint = Blueprint('enrollment', __name__)


@enrollment_blueprint.route('/', methods=['POST'])
def enroll_student():
    data = request.json
    new_enrollment = StudentSubject(**data)
    db.session.add(new_enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment added successfully!"}), 201


@enrollment_blueprint.route('/<int:student_id>', methods=['GET'])
def get_enrollments(student_id):
    enrollments = StudentSubject.query.filter_by(student_id=student_id).all()
    return jsonify([{
        'id': e.id,
        'student_id': e.student_id,
        'subject_id': e.subject_id,
        'semester': e.semester,
        'year': e.year,
        'grade': e.grade
    } for e in enrollments])


@enrollment_blueprint.route('/', methods=['GET'])
def get_all_enrollments():
    enrollments = StudentSubject.query.all()
    return jsonify([{
        'id': e.id,
        'student_id': e.student_id,
        'subject_id': e.subject_id,
        'semester': e.semester,
        'year': e.year,
        'grade': e.grade
    } for e in enrollments])


@enrollment_blueprint.route('/<int:id>', methods=['PUT'])
def update_enrollment(id):
    enrollment = StudentSubject.query.get(id)
    if not enrollment:
        return jsonify({"error": "Enrollment not found"}), 404

    data = request.json
    for key, value in data.items():
        setattr(enrollment, key, value)

    db.session.commit()
    return jsonify({"message": "Enrollment updated successfully!"})


@enrollment_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_enrollment(id):
    enrollment = StudentSubject.query.get(id)
    if not enrollment:
        return jsonify({"error": "Enrollment not found"}), 404

    db.session.delete(enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment deleted successfully!"})
