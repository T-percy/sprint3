from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('pages/inicio.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template('pages/login.html')

@app.route('/registro/', methods=["GET", "POST"])
def register():
    return render_template('pages/registro.html')

@app.route('/perfil/', methods=["GET", "POST"])
def profile():
    return render_template('pages/perfil.html')

@app.route('/dashboard/', methods=["GET", "POST"])
def dashboard():
    return render_template('pages/dashboard.html')

@app.route('/menu/', methods=["GET", "POST"])
def menu():
    return render_template('pages/menu.html')

@app.route('/plato/', methods=["GET", "POST"])
def plato():
    return render_template('pages/plato.html')

@app.route('/resultado_busqueda/', methods=["GET"])
def found():
    return render_template('pages/resultado_busqueda.html')

@app.route('/pedido/', methods=["GET", "POST"])
def order():
    return render_template('pages/pedido.html')

@app.route('/lista_deseo/', methods=["GET", "POST"])
def list_wish():
    return render_template('pages/lista_deseo.html')