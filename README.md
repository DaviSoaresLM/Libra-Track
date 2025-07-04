```markdown
# 📚 LibraTrack - Sistema de Biblioteca

**LibraTrack** é um sistema de gerenciamento de bibliotecas desenvolvido em Python com conexão ao banco de dados MySQL via **PyMySQL**. O sistema permite controlar livros, autores, editoras, usuários e empréstimos de maneira eficiente.

## ✨ Funcionalidades

- Cadastro e consulta de **livros**, **autores**, **editoras** e **usuários**
- Registro de **empréstimos** e **devoluções**
- Verificação de **disponibilidade** de livros
- Integração total com banco de dados MySQL

## 🛠️ Tecnologias

- 🐍 **Python 3.x**
- 🐬 **MySQL** (banco de dados relacional)
- 🔌 **PyMySQL** (conector Python-MySQL)
- 🛠️ DBeaver (opcional para modelagem e administração do banco)

## 📁 Estrutura do Projeto

```

LibraTrack/
│
├── scripts/                   # Scripts SQL do banco
│   ├── create\_tables.sql
│   └── insert\_data.sql
│
├── lib/                       # Código-fonte Python
│   ├── db.py                  # Conexão e utilitários com MySQL via PyMySQL
│   ├── models/                # Lógica de cada entidade (livros, autores, etc.)
│   └── main.py                # Arquivo principal de execução
│
├── requirements.txt           # Dependências do projeto
└── README.md

````

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/LibraTrack.git
cd LibraTrack
````

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o banco de dados MySQL:

* Crie um banco chamado `libratrack`
* Execute os scripts em `scripts/create_tables.sql` e (opcionalmente) `insert_data.sql`

4. Configure seu acesso ao banco em `lib/db.py`:

```python
connection = pymysql.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='libratrack'
)
```

5. Execute o sistema:

```bash
python lib/main.py
```

## 📌 Melhorias Futuras

* [ ] Interface gráfica com Tkinter ou Web com Flask
* [ ] Criação de relatórios de empréstimos
* [ ] Validações de entrada e tratamento de exceções
* [ ] Autenticação de usuários

## 👨‍💻 Desenvolvedor

* [DaviSoaresLM](https://github.com/DaviSoaresLM)

---

> Projeto educacional com foco em manipulação de banco de dados MySQL via Python.

```

---

Se quiser, posso montar para você os arquivos iniciais `db.py` e `main.py` com conexão e exemplo de consulta. Deseja isso?
```
