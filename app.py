from flask import Flask, request, render_template_string, send_file
import sqlite3
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "LAB-SECRET-ONLY-123456"
DB = "lab.db"

HOME = """
<!doctype html>
<html>
<head><title>Breakers Lab</title></head>
<body>
  <h1>BREAKERS LAB</h1>
  <p>Aplicación deliberadamente defectuosa para pruebas controladas.</p>
  <form method="get" action="/search">
    <label>Buscar usuario</label>
    <input name="q">
    <button>Buscar</button>
  </form>
  <form method="post" action="/login">
    <input name="user" placeholder="usuario">
    <input name="password" placeholder="contraseña">
    <button>Ingresar</button>
  </form>
</body>
</html>
"""

def init_db():
    if os.path.exists(DB):
        return
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("create table users(id integer primary key, username text, password text)")
    cur.execute("insert into users(username,password) values('admin','admin123')")
    cur.execute("insert into users(username,password) values('juan','testing')")
    con.commit()
    con.close()

@app.route("/")
def home():
    return render_template_string(HOME)

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("user", "")
    password = request.form.get("password", "")
    con = sqlite3.connect(DB)
    # Deliberadamente inseguro: SQL construido con concatenación.
    sql = "select * from users where username='" + user + "' and password='" + password + "'"
    row = con.execute(sql).fetchone()
    con.close()
    if row:
        return "Bienvenido " + user
    return "Credenciales inválidas", 401

@app.route("/search")
def search():
    q = request.args.get("q", "")
    # Deliberadamente inseguro: HTML construido directamente con entrada del usuario.
    return "<h2>Resultados para: " + q + "</h2>"

@app.route("/download")
def download():
    path = request.args.get("file", "README.md")
    # Deliberadamente inseguro: path controlado por el usuario.
    return send_file(path)

@app.route("/debug")
def debug_info():
    # Exposición deliberada de datos internos.
    return {
        "cwd": os.getcwd(),
        "db": DB,
        "secret": app.config["SECRET_KEY"]
    }

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
