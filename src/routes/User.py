from flask import Blueprint, jsonify, request

# Entities
from models.entities.User import User, UserConfirm

# Models
from models.UserModels import UserModel

users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/add', methods=['POST'])
def add_user():
    try:
        full_name = request.json['Nombre Completo']
        email = request.json['Correo']
        password = request.json['Contraseña']
        address = request.json['Dirección']
        phone = request.json['Teléfono']
        birth_date = request.json['Fecha de nacimiento']

        user = User(full_name, email, password, address, phone, birth_date)
        affected_rows = UserModel.add_user(user)

        if affected_rows == 1:
            return jsonify({'Message': 'User Created Suscessfuly'})
        else:
            return jsonify({'Message': 'Error creating User'}), 500
    except Exception as e:
        return jsonify({'Message': str(e)}), 500

@users_bp.route('/login/<email>&<password>')
def login_user(email, password):
    try:
        user = UserConfirm(email, password)
        affected_row = UserModel.login_user(user)

        if affected_row == 1:
            return jsonify({"Message": "Welcome, user"})
        else:
            return jsonify({"Message":"User or password incorrect"}),404
    except Exception as e:
        return jsonify({"Message": str(e)})


