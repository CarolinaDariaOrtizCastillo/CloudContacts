from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pymysql

app = Flask(__name__)

# -------------------------
# CONEXIÓN A MYSQL
# -------------------------

print("Iniciando conexión con MySQL desde EC2...")

def get_db():
    host = "98.93.1.88"           # IP pública EC2
    user = "admin"
    password = "CaroOrtizCas12"   # revisa que no haya espacios al inicio o final
    database = "form_contact"

    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connect_timeout=10
        )
        return conn
    except pymysql.err.OperationalError as e:
        print("❌ Error operativo:", e)
    except pymysql.err.InternalError as e:
        print("❌ Error interno:", e)
    except Exception as e:
        print("❌ Otro error:", e)
    return None

# -------------------------
# USUARIO AUTORIZADO
# -------------------------
ALLOWED_EMAIL = "admin@vg.edu"
ALLOWED_PASS = "SuperClave123"

# -------------------------
# RUTAS HTML
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacts")
def login_contacts():
    return render_template("login_contacts.html")

@app.route("/contacts-real")
def contacts_page():
    return render_template("contacts.html")

# -------------------------
# API: REGISTRO DE CONTACTO
# -------------------------
@app.route("/api/add-contact", methods=["POST"])
def add_contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    if not name or not email:
        return jsonify({"saved": False, "error": "Nombre y correo son obligatorios."})

    db = get_db()
    if db is None:
        return jsonify({"saved": False, "error": "No se pudo conectar a la base de datos."})

    try:
        cursor = db.cursor()
        sql = """
            INSERT INTO contact (name, email, cellphone)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (name, email, phone))
        db.commit()
        return jsonify({"saved": True})
    except Exception as e:
        return jsonify({"saved": False, "error": str(e)})
    finally:
        if cursor: cursor.close()
        if db: db.close()

# -------------------------
# API: OBTENER CONTACTOS
# -------------------------
@app.route("/api/contacts")
def get_contacts():
    db = get_db()
    if db is None:
        return jsonify({"error": "No se pudo conectar a la base de datos."})

    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contact")
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        if cursor: cursor.close()
        if db: db.close()

# -------------------------
# AUTH PARA LISTA
# -------------------------
@app.route("/auth-contacts", methods=["POST"])
def auth_contacts():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if email == ALLOWED_EMAIL and password == ALLOWED_PASS:
        return jsonify({"allowed": True})
    return jsonify({"allowed": False})

# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
