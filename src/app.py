from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/inicio.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template('pages/login.html')

@app.route('/registro/')
def register():
    return render_template('pages/registro.html')

@app.route('/perfil/')
def profile():
    return render_template('pages/perfil.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('pages/dashboard.html')

@app.route('/menu/')
def menu():
    return render_template('pages/menu.html')

@app.route('/plato/')
def plato():
    return render_template('pages/plato.html')

@app.route('/resultado_busqueda/')
def found():
    return render_template('pages/resultado_busqueda.html')

@app.route('/pedido/')
def order():
    return render_template('pages/pedido.html')

@app.route('/lista_deseo/')
def list_wish():
    return render_template('pages/lista_deseo.html')