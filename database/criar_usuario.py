from database.connection import Database

db = Database()
conn = db.conectar()
cursor = conn.cursor()

cursor.execute("""
INSERT INTO usuarios (username, senha)
VALUES (?, ?)
""", ("admin", "1234"))

conn.commit()
conn.close()

print("Rodando criação de usuário...")