from flask import Blueprint, jsonify, request
from models import db
from models.student_register import Student
from models.class_model import Class

# Tạo Blueprint cho student
student_blueprint = Blueprint('student', __name__)


@student_blueprint.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()

    result = []
    for student in students:
        result.append({
            "id": student.id,
            "f_name": student.f_name,
            "l_name": student.l_name,
            "year": student.year,
            "age": student.age,
            "gender": student.gender,
            "birth": student.birth,
            "contact": student.contact,
            "email": student.email,
            "class_name": student.class_.name if student.class_ else None  # Trả về class_name
        })

    return jsonify(result)


@student_blueprint.route('/', methods=['POST'])
def add_student():
    data = request.json

    # Lấy class_id từ class_name
    class_id = data.get("class_id")
    class_obj = Class.query.filter_by(id=class_id).first()
    if not class_obj:
        return jsonify({"error": "Class not found"}), 404

    student = Student(
        f_name=data.get("f_name"),
        l_name=data.get("l_name"),
        year=data.get("year"),
        age=data.get("age"),
        gender=data.get("gender"),
        birth=data.get("birth"),
        contact=data.get("contact"),
        email=data.get("email"),
        class_id=class_obj.id  # Lưu class_id thay vì class_name
    )

    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student added successfully!"}), 201


@ student_blueprint.route('/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if student:
        return jsonify({
            "id": student.id,
            "f_name": student.f_name,
            "l_name": student.l_name,
            "year": student.year,
            "age": student.age,
            "gender": student.gender,
            "birth": student.birth,
            "contact": student.contact,
            "email": student.email,
            "class_name": student.class_.name if student.class_ else None  # Trả về class_name
        })
    return jsonify({"error": "Student not found"}), 404


@ student_blueprint.route('/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.json

    # Lấy class_id từ class_name
    class_name = data.get("class_name")
    if class_name:
        class_obj = Class.query.filter_by(name=class_name).first()
        if not class_obj:
            return jsonify({"error": "Class not found"}), 404
        student.class_id = class_obj.id

    student.f_name = data.get("f_name", student.f_name)
    student.l_name = data.get("l_name", student.l_name)
    student.year = data.get("year", student.year)
    student.age = data.get("age", student.age)
    student.gender = data.get("gender", student.gender)
    student.birth = data.get("birth", student.birth)
    student.contact = data.get("contact", student.contact)
    student.email = data.get("email", student.email)

    db.session.commit()
    return jsonify({"message": "Student updated successfully!"})


@ student_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully!"})
