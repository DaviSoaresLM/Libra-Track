from lib.db import get_connection


# Criação do banco
def criar_banco():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS LibraTrack")
            cursor.execute("USE LibraTrack")
            conn.commit()
            print("Banco de dados criado/verificado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar banco: {e}")
        finally:
            conn.close()
    else:
        print("Conexão falhou. Banco não foi criado.")


# Chamada p/ verificação do comando
if __name__ == "__main__":
    criar_banco()
