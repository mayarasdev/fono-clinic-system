from flask import Blueprint, render_template, request, redirect, session
from database.connection import Database
import os

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        db = Database()
        conn = db.conectar()
        cursor = conn.cursor()

        print("BANCO USADO:", os.path.abspath("database.db"))

        cursor.execute("""
SELECT * FROM usuarios WHERE email = ? AND senha = ?
""", (email, senha))

        user = cursor.fetchone()
        conn.close()

        if user:
            session["usuario"] = email
            return redirect("/dashboard")
        else:
            return "Login inválido"

    return render_template("login.html")