from flask import Flask, render_template
from flask import request, abort
app = Flask(__name__)

@app.route('/')
def put_static_image():
    cadena = 'src=/static/inosuke.jpg alt="A devil slayer"'

    return render_template('index.html', mensage=cadena)

@app.route('/user/<username>')
def perfil_usuario(username):
    return render_template('usuarios.html', user=username)

@app.route('/saludo')
def saludo_parametros():
    par1 = request.args.get('x')
    par2 = request.args.get('y')
    cad = "("+par1+", "+par2+")"
    return render_template('parametros.html', param=cad)

@app.errorhandler(404)
def error_404(error):
    return "Error 404, page not found", 404
