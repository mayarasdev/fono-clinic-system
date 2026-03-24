from database.connection import Database

db = Database()
conn = db.conectar()
cursor = conn.cursor()
from database.connection import Database

db = Database()
conn = db.conectar()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

conn.commit()
conn.close()

print("Tabela patients criada!")

cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    senha TEXT
)
""")

cursor.execute("""
INSERT INTO usuarios (nome, email, senha)
VALUES ('Admin', 'admin@email.com', '123456')
""")

conn.commit()
conn.close()

print("BANCO CRIADO CERTO!")