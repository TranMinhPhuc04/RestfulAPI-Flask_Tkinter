from flask import Blueprint, jsonify, request
from models import db
from models.subject import Subject

subject_blueprint = Blueprint('subject', __name__)

@subject_blueprint.route('/', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'credits': s.credits
    } for s in subjects])

@subject_blueprint.route('/', methods=['POST'])
def add_subject():
    data = request.json
    new_subject = Subject(**data)
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({"message": "Subject added successfully!"}), 201

@subject_blueprint.route('/<int:id>', methods=['GET'])
def get_subject(id):
    subject = Subject.query.get(id)
    if subject:
        return jsonify({
            'id': subject.id,
            'name': subject.name,
            'credits': subject.credits
        })
    return jsonify({"error": "Subject not found"}), 404

@subject_blueprint.route('/<int:id>', methods=['PUT'])
def update_subject(id):
    subject = Subject.query.get(id)
    if not subject:
        return jsonify({"error": "Subject not found"}), 404
    
    data = request.json
    for key, value in data.items():
        setattr(subject, key, value)
    
    db.session.commit()
    return jsonify({"message": "Subject updated successfully!"})

@subject_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_subject(id):
    subject = Subject.query.get(id)
    if not subject:
        return jsonify({"error": "Subject not found"}), 404
    
    db.session.delete(subject)
    db.session.commit()
    return jsonify({"message": "Subject deleted successfully!"})
