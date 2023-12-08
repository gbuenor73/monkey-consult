import mysql.connector

db_config = {
    'host': "localhost",
    'user': "monkey",
    'password': "monkey",
    'database': "monkey_consulting"
}


def connect():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Conectado com Mysql')
            return conn
    except mysql.connector.Error as e:
        print(f'Erro ao conectar com o MYSQL: {e}')
        return None
