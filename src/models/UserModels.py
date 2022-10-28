from database.db import get_connection
from .entities.User import User, UserConfirm


class UserModel():

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios("Nombre Completo", "Correo", "Contraseña", "Dirección", "Teléfono", "Fecha de nacimiento")
                                    VALUES(%s, %s, %s,%s,%s,%s)""", (user.full_name, user.email, user.password, user.address, user.phone, user.birth_date))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)

    @classmethod
    def login_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT "Correo", "Contraseña" FROM usuarios
                    WHERE "Correo" = %s AND "Contraseña"= %s """, (user.email, user.password))

                row = cursor.fetchone()
                user = None

                if row != None:
                    user = UserConfirm(row[0], row[1])
                    user = user.to_json()

            connection.close()
            return user
        except Exception as e:
            raise Exception(e)
