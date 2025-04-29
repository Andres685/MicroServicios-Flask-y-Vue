from flask import Blueprint, request, jsonify
from .models import db, User

routes = Blueprint('routes', __name__)

@routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email') 
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Faltan datos'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'El usuario ya existe'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'El email ya está registrado'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario creado correctamente'}), 201

@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Faltan datos'}), 400

    user = User.query.filter_by(email = email).first()

    if user and user.check_password(password):
        return jsonify({
            'message': 'Login exitoso',
            'user_id': user.id,
            'username': user.username
        }), 200

    return jsonify({'message': 'Usuario o contraseña incorrecta'}), 401