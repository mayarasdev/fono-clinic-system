from database.connection import Database


class Paciente:

    def cadastrar(nome, idade, telefone, observacoes):
        db = Database()
        conn = db.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO pacientes (nome, idade, telefone, observacoes)
        VALUES (?, ?, ?, ?)
        """, (nome, idade, telefone, observacoes))

        conn.commit()
        conn.close()


    def listar():
        db = Database()
        conn = db.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pacientes")

        pacientes = cursor.fetchall()

        conn.close()

        return pacientes