from flask import Flask, render_template, request, flash
from flask.json.tag import PassDict
from markupsafe import escape # Evitar inyección de código
import os

from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=["GET"])
@app.route('/index/', methods=["GET"])
@app.route('/inicio/', methods=["GET"])
@app.route('/home/', methods=["GET"])
def index():
    return render_template('pages/inicio.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method=='GET':
        return render_template('pages/login.html')
    else:
        user = escape(request.form["usuario"])#verificar con el formulario
        password = escape(request.form["contraseña"])#Verificar con el formulario
    #Validar
    salida = ''
    if len(user.strip())<1 or len(user.strip())>8:
        salida += 'El usuario es requerido y debe tener entre 1 y 8 caracteres'
    if len(password.strip())<1 or len(password.strip())>8:
        salida += 'La contraseña es requerida y debe tener entre 1 y 8 caracteres'
    return redirect('pages/pedido.html')

@app.route('/registro/', methods=["GET", "POST"])
def register():
    if request.method=='GET':
        return render_template('pages/registro.html')
    else:
        nombres = escape(request.form["nombres"]) 
        apellidos = escape(request.form["apellidos"]) 
        tipo_identificacion = escape(request.form["tipo_identificacion"]) 
        identificacion = escape(request.form["identificacion"]) 
        genero = escape(request.form["genero"]) 
        direccion = escape(request.form["direccion"]) 
        pais = escape(request.form["pais"]) 
        ciudad = escape(request.form["ciudad"]) 
        telefono = escape(request.form["telefono"]) 
        fecha_nacimiento = escape(request.form["fecha_nacimiento"]) 
        acpterminos = escape(request.form["acpterminos"]) 
    
    return redirect('pages/login.html')

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