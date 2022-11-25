from flask import Blueprint, jsonify, request

# Entities
from models.entities.User import User, UserConfirmation

# Models
from models.UserModels import UserModel

# Lib

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

@users_bp.route('/users')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as e:
        return jsonify({'Message': str(e)}), 500


@users_bp.route('/login/', methods=['POST'])
def login_user():
    try:
        email = request.json['correo']
        password = request.json['contraseña']
        user = UserConfirmation(email, password)
        affected_row = UserModel.login_user(user)
        if affected_row != None:
            return jsonify({"Message": "Welcome, {}".format(affected_row['correo'])})
        else:
            return jsonify({"Message":"User or password incorrect"}),404
    except Exception as e:
        return jsonify({"Message": str(e)})


