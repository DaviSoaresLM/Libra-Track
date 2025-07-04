# Criação e gerenciamento de conexão com o banco de dados MySQL usando pymysql

import pymysql


# Módulo para gerenciar a conexão com o banco de dados MySQL usando pymysql
def get_connection(database=None):
    try:
        conn = pymysql.connect(
            host="localhost", user="davi", password="8898", database=database
        )
        print("Conexão com o banco de dados estabelecida!")
        return conn

    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Teste de conexão com o banco de dados

if __name__ == "__main__":
    try:
        conn = get_connection()
        if conn:
            print("Conexão de teste OK.")
            conn.close()
    except Exception as e:
        print(f"Erro inesperado: {e}")
