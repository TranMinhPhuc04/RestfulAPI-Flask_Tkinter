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
    } for c in classes])

@class_blueprint.route('/', methods=['POST'])
def add_class():
    data = request.json
    new_class = Class(**data)
    db.session.add(new_class)
    db.session.commit()
    return jsonify({"message": "Class added successfully!"}), 201

@class_blueprint.route('/<int:id>', methods=['GET'])
def get_class(id):
    class_instance = Class.query.get(id)
    if class_instance:
        return jsonify({
            'id': class_instance.id,
            'name': class_instance.name,
            'faculty': class_instance.faculty
        })
    return jsonify({"error": "Class not found"}), 404

@class_blueprint.route('/<int:id>', methods=['PUT'])
def update_class(id):
    class_instance = Class.query.get(id)
    if not class_instance:
        return jsonify({"error": "Class not found"}), 404
    
    data = request.json
    for key, value in data.items():
        setattr(class_instance, key, value)
    
    db.session.commit()
    return jsonify({"message": "Class updated successfully!"})

@class_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_class(id):
    class_instance = Class.query.get(id)
    if not class_instance:
        return jsonify({"error": "Class not found"}), 404
    
    db.session.delete(class_instance)
    db.session.commit()
    return jsonify({"message": "Class deleted successfully!"})
