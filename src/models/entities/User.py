from utils.DateFormat import DateFormat


class User():

    def __init__(self, full_name, email, password, address, phone, birth_date):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone
        self.birth_date = birth_date

    def to_json(self):
        return {
            'Nombre Completo': self.full_name,
            'Correo': self.email,
            'Contraseña': self.password,
            'Dirección': self.address,
            'Teléfono': self.phone,
            'Fecha de Nacimiento': DateFormat.convert_date(self.birth_date)
        }


class UserConfirm():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def to_json(self):
        return {
            'Correo': self.email,
            'Contraseña': self.password
        }
