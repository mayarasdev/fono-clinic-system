import sqlite3
import os

class Database:
    def conectar(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, '..', 'database.db')

        print("USANDO BANCO EM:", db_path)  # debug

        conn = sqlite3.connect(db_path)
        return conn