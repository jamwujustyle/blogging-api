import requests 
import psycopg2
print(requests)

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname = 'blogging',
            user = 'postgres',
            password = '0880',
            host = 'localhost',
            port=5432
        )
        if conn:
            print(f"connection established successfully at port")
        else:
            print('error connecting to database')
    except Exception as ex:
        print(f"error {ex}")