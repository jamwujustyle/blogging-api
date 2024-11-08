import requests 
import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname = 'blogging',
            user = 'postgres',
            password = '0880',
            host = 'localhost',
            port=5432
        )
        return conn

    except Exception as ex:
        print(f"error {ex}")
        raise