import os
import psycopg2
from decouple import config

conn = psycopg2.connect(
    host=config('HOST'),
    database=config('DATABASE'),
    user=config('USER'),
    password=config('PASSWORD'))

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS usuarios;')
cur.execute('CREATE TABLE usuarios (id serial PRIMARY KEY,'
                                    'Nombre_Completo varchar (150) NOT NULL,'     
                                    'Correo varchar (150) NOT NULL,' 
                                    'Contraseña varchar (255) NOT NULL,' 
                                    'Dirección varchar (150) NOT NULL,' 
                                    'Teléfono bigint NOT NULL,' 
                                    'Fecha_de_nacimiento date NOT NULL);'
                                    )

    
cur.execute('INSERT INTO usuarios (Nombre_Completo, Correo, Contraseña, Dirección, Teléfono, Fecha_de_nacimiento)'
                                    'VALUES(%s, %s, %s,%s,%s,%s)', 
                                    ('Juan Perez', 
                                    'example@gmail.com',
                                    '123456',
                                    'Calle 123', 
                                    123456, 
                                    "1990-01-01")
                                    )

conn.commit()

cur.close()
conn.close()