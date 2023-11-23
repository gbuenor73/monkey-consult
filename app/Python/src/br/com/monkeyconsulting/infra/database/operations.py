import mysql.connector
from .config import db_config


def connect():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Conectado com Mysql')
            return conn
    except mysql.connector.Error as e:
        print(f'Erro ao conectar com o MYSQL: {e}')
        return None


def fetch_data(query):
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except mysql.connector.Error as e:
            print(f"Erro ao executar comando sql: {e}")
            return None
