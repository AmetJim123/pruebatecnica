from utils.DateFormat import DateFormat
from werkzeug.security import check_password_hash, generate_password_hash

class User():

    def __init__(self, full_name, email, password, address, phone, birth_date):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone
        self.birth_date = birth_date

    

    @classmethod
    def hash_password(self, password):
        return generate_password_hash(password)

    def to_json(self):
        return {
            'Nombre Completo': self.full_name,
            'Correo': self.email,
            'Contraseña': self.password,
            'Dirección': self.address,
            'Teléfono': self.phone,
            'Fecha de Nacimiento': DateFormat.convert_date(self.birth_date)
        }
    
    def __repr__(self):
        return str(self.__dict__)

class UserConfirmation():

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
        
    def to_json(self):
        return {
            'Correo': self.email,
            'Contraseña': self.password
        }