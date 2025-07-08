# Inserir dados no banco de dados PostgreSQL
import psycopg2
from lib.db import get_connection
conn = get_connection()
cursor = conn.cursor()

# Criação da tabela Autor
cursor.execute('''CREATE TABLE IF NOT EXISTS autor(
                  id_autor SERIAL,
                  nome_autor VARCHAR(255) NOT NULL,
                  pais_autor VARCHAR(255),
                  data_nascimento DATE NOT NULL,
                  idade_autor INT NOT NULL);''')

# Criação da tabela Editora
cursor.execute('''CREATE TABLE IF NOT EXISTS editora(
                  id_editora SERIAL,
                  nome_editora VARCHAR(255) NOT NULL,
                  pais_editora VARCHAR(255),
                  cnpj VARCHAR(50),
                  telefone VARCHAR(50));''')

conn.commit()
conn.close()
