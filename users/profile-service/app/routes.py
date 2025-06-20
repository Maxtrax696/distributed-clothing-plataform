from flask import Blueprint, request, jsonify
from .models import Profile
from .db import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profiles', methods=['POST'])
def create_profile():
    data = request.json
    new_profile = Profile(name=data['name'], email=data['email'], bio=data.get('bio'))
    db.session.add(new_profile)
    db.session.commit()
    return jsonify({'message': 'Profile created'}), 201

@profile_bp.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([{
        'id': p.id, 'name': p.name, 'email': p.email, 'bio': p.bio
    } for p in profiles])
