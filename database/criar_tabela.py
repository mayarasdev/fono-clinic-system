def criar_tabela(self):
    conn = self.conectar()
    cursor = conn.cursor()

    # Pacientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        telefone TEXT,
        observacoes TEXT
    )
    """)

    # Usuários (login)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        senha TEXT
    )
    """)

    conn.commit()
    conn.close()
    
    from database.connection import Database

db = Database()
db.criar_tabela()

print("Tabela criada com sucesso!")