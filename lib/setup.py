# -*- coding: utf-8 -*-

import psycopg2
from lib.db import get_connection


def criar_banco():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'libratrack'")
            exists = cursor.fetchone()

            if not exists:
                cursor.execute('CREATE DATABASE "LibraTrack"')
                print("Banco de dados 'LibraTrack' criado com sucesso!")
            else:
                print("Banco de dados 'LibraTrack' ja existe.")
        except Exception as e:
            print(f"Erro ao criar o banco de dados: {e}")
        finally:
            conn.close()
    else:
        print("Falha ao conectar. Banco nao foi criado.")

if __name__ == "__main__":
    criar_banco()
