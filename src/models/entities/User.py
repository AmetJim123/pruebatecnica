from utils.DateFormat import DateFormat


class User():

    def __init__(self, full_name, email, password, address, phone, birth_date, token=None):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone
        self.birth_date = birth_date
        self.token = token
    

    def to_json(self):
        return {
            'nombre_completo': self.full_name,
            'correo': self.email,
            'contraseña': self.password,
            'dirección': self.address,
            'teléfono': self.phone,
            'fecha_de_nacimiento': DateFormat.convert_date(self.birth_date)
        }
    
    def __repr__(self):
        return str(self.__dict__)

class UserConfirmation():

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def to_json(self):
        return {
            'correo': self.email,
            'contraseña': self.password
        }
