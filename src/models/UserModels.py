from database.db import get_connection
from .entities.User import User, UserConfirmation
from lib.generate_token import generate_token, decode_token
import traceback


class UserModel():

    @classmethod
    def add_user(self, user):
        print('************')
        print(user)
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
            print(traceback.format_exc())
            raise Exception(e)

    @classmethod
    def login_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                password = generate_token(user.password, user.email)
                cursor.execute("""SELECT "Correo", "Contraseña" FROM usuarios
                    WHERE "Correo" = %s AND "Contraseña" = %s """, (user.email, password))

                row = cursor.fetchone()
                user = None
                if row != None:
                    email = row[0]
                    password = row[1]
                    password = decode_token(password, email)
                    user = UserConfirmation(email,password)
                    user = user.to_json()

            connection.close()
            return user
        except Exception as e:
            print(traceback.format_exc())
            raise Exception(e)

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            all_users = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM usuarios""")

                result_set = cursor.fetchall()

                for row in result_set:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    all_users.append(user.to_json())

            connection.close()
            return all_users
        except Exception as e:
            raise Exception(e)