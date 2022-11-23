import psycopg2
from psycopg2 import DatabaseError
from decouple import config
import traceback

def get_connection():
    try:
        return psycopg2.connect(
            host=config('HOST'),
            database=config('DATABASE'),
            user=config('USER'),
            password=config('PASSWORD'))
        
    except DatabaseError as e:
        print(traceback.format_exc())
        return e
