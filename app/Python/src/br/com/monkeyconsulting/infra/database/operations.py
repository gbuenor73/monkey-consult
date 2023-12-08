import mysql.connector

from app.Python.src.br.com.monkeyconsulting.infra.database.config import connect


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
