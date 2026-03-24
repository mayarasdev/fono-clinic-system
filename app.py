from flask import Flask
from routes.auth_routes import auth_bp
from routes.patient_routes import patient_bp

app = Flask(__name__)
app.secret_key = "123456"

app.register_blueprint(auth_bp)
app.register_blueprint(patient_bp)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)