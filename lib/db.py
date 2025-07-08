import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost", # Adiciona o host
            user="user", # Adiciona o usuário que irá acessar o banco
            password="password", # Adiciona a senha do usuário
            dbname="dbname" # Nome do banco que será utilizado        )
        conn.set_session(autocommit=True)
        print("Conexao com o banco 'postgres' estabelecida!")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None
