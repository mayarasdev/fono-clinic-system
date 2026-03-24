import sqlite3

conn = sqlite3.connect('database.db')

# Criar tabela de usuários
conn.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

# Criar usuário de teste
conn.execute("""
INSERT INTO usuarios (nome, email, senha)
VALUES (?, ?, ?)
""", ("Admin", "admin@email.com", "123456"))

conn.commit()
conn.close()

print("Banco configurado com sucesso!")