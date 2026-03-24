from flask import Blueprint, render_template
from database.connection import Database

patient_bp = Blueprint("patients", __name__)

@patient_bp.route("/patients")
def listar_pacientes():
    db = Database()
    conn = db.conectar()
    cursor = conn.cursor()

    pacientes = cursor.execute("SELECT * FROM patients").fetchall()

    conn.close()

    return render_template("patients.html", pacientes=pacientes)