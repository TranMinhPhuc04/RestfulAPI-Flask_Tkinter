from flask import Blueprint, jsonify, request
from models import db
from models.class_model import Class

class_blueprint = Blueprint('class', __name__)


@class_blueprint.route('/', methods=['GET'])
def get_classes():
    classes = Class.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'faculty': c.faculty
    } for c in classes]), 200


@class_blueprint.route('/', methods=['POST'])
def add_class():
    data = request.json
    if not data or not data.get('name') or not data.get('faculty'):
        return jsonify({"error": "Name and Faculty are required"}), 400

    new_class = Class(name=data['name'], faculty=data['faculty'])
    db.session.add(new_class)

    try:
        db.session.commit()
        return jsonify({"message": "Class added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@class_blueprint.route('/<int:id>', methods=['GET'])
def get_class(id):
    class_instance = Class.query.get(id)
    if not class_instance:
        return jsonify({"error": "Class not found"}), 404

    return jsonify({
        'id': class_instance.id,
        'name': class_instance.name,
        'faculty': class_instance.faculty
    }), 200


@class_blueprint.route('/<int:id>', methods=['PUT'])
def update_class(id):
    class_instance = Class.query.get(id)
    if not class_instance:
        return jsonify({"error": "Class not found"}), 404

    data = request.json
    if 'name' in data:
        class_instance.name = data['name']
    if 'faculty' in data:
        class_instance.faculty = data['faculty']

    try:
        db.session.commit()
        return jsonify({"message": "Class updated successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@class_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_class(id):
    class_instance = Class.query.get(id)
    if not class_instance:
        return jsonify({"error": "Class not found"}), 404

    db.session.delete(class_instance)

    try:
        db.session.commit()
        return jsonify({"message": "Class deleted successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
