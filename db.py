import psycopg2
from psycopg2 import pool
import logging
def logging_config():
    # Set up logging to console only
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Change this level as needed (DEBUG, ERROR, etc.)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Global logging level for all handlers
    logger.addHandler(console_handler)



connection_pool = None

def get_connection():
    global connection_pool
    if connection_pool is None:
        try:
            connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 20,
                dbname='blogging',
                user='postgres',
                password='0880',
                host='localhost',
                port=5432
            )
            logging.info('connection pool created successfully')
        except Exception as ex:
            logging.error(f'error creating connection pool: {ex}')
            raise
    try:
        return connection_pool.getconn()
    except Exception as ex:
        logging.error(f'error getting connection from pool: {ex}') 
        raise 

def release_connection(conn):
    try:
        if connection_pool:
            connection_pool.putconn(conn)
            logging.info('connection released back to pool')
    except Exception as ex:
        logging.error(f'error releasing connection: {ex}')
        raise