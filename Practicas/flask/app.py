from flask import Flask, render_template, session, request, abort, redirect, url_for, escape
from PIL import Image, ImageDraw
import os, sys, random, re
from pickleshare import *
from pymongo import MongoClient
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
cliente = MongoClient("mongo", 27017)
base_datos = cliente.SampleCollections
tabla_pkm = cliente.database

################################################################################
#
# PRÁCTICA 2
#
################################################################################

# Muestra una página estática con una hoja de estilo y una fotografía
@app.route('/')
def put_static_image():
    cadena = 'src=/static/images/inosuke.jpg alt="A devil slayer"'

    return render_template('index.html', mensage=cadena)

# Muestra páginas saludando según el usuario que ha entrado
@app.route('/user/<username>')
def perfil_usuario(username):
    return render_template('usuarios.html', user=username)

# Muestra una página saludando y mostrando los parámetros que se han introducido en la url
@app.route('/saludo')
def saludo_parametros():
    par1 = request.args.get('x')
    par2 = request.args.get('y')
    cad = "("+par1+", "+par2+")"
    return render_template('parametros.html', param=cad)

# Muestra un formulario para introducir las coordenadas para calcular el fractal
@app.route('/mandelbrot')
def mandelbrot():
    return render_template('mandelbrot.html')

# Muestra el fractal de mandelbrot
@app.route('/imagenmandelbrot')
def imagen_mandelbrot():
    RE_START = -2
    RE_END = 1
    IM_START = -1
    IM_END = 1
    ANCHO = 1024
    ALTO = 750

    x1 = int(request.args.get('x1'))
    y1 = int(request.args.get('y1'))
    x2 = int(request.args.get('x2'))
    y2 = int(request.args.get('y2'))

    print(x1)

    if x1>x2:
        mayor_x = x1
        menor_x = x2

    else:
        mayor_x = x2
        menor_x = x1

    if y1>y2:
        mayor_y = y1
        menor_y = y2

    else:
        mayor_y = y2
        menor_y = y1

    img = Image.new('RGB', (ANCHO, ALTO), (0,0,0))
    mdb = ImageDraw.Draw(img)

    for i in range(menor_x, mayor_x):
        for j in range(menor_y, mayor_y):
            complejo = complex(RE_START+(i/ANCHO)*(RE_END-RE_START), IM_START+(j/ALTO)*(IM_END-IM_START))

            m = mandelbrot(complejo)
            color = 255 - int(m*255/100)
            mdb.point([i,j], (color,color,color))

    for filename in os.listdir('static/images/'):
        if filename.startswith('img_mdb'):
            os.remove('static/images/' + filename)

    nombre_img = 'static/images/img_mdb'+str(x1)+str(y1)+str(x2)+str(y2)+'.png'
    img.save(nombre_img)
    cad = 'src='+nombre_img+' alt="Imagen del fractal"'
    return render_template('mostrar_mandelbrot.html', imagen=cad)

# Muestra una página de error
@app.errorhandler(404)
def error_404(error):
    return "Error 404, page not found", 404

# Función auxiliar para calcular el valor del fractal de mandelbrot
def mandelbrot(c):
    z = 0
    n = 0

    while abs(z) <= 2 and n < 100:
        z = z*z + c
        n += 1

    return n

@app.route('/svg')
def random_svg():
    figuras=['circle', 'rect']
    colores=['red', 'green', 'blue', 'black', 'orange', 'violet', 'purple', 'yellow', 'fuchsia', 'snow', 'darkRed', 'coral', 'mediumPurple', 'orangeRed', 'navy', 'saddleBrown', 'cyan']

    forma = random.choice(figuras)
    color = random.choice(colores)
    color_relleno = random.choice(colores)

    fig=forma

    if forma=='circle':
        cx = random.randint(50, 200)
        cy = random.randint(50, 200)
        r = random.randint(30, 80)
        fig=fig+' cx='+str(cx)+' cy='+str(cy)+' r='+str(r)

    elif forma=='rect':
        x = random.randint(10, 150)
        y = random.randint(10, 150)
        width = random.randint(50, 200)
        height = random.randint(50, 200)
        fig=fig+' x='+str(x)+' y='+str(y)+' width='+str(width)+' height='+str(height)

    fig=fig+' stroke='+color+' stroke-width=4 fill='+color_relleno

    return render_template('mostrar_svg.html', figura=fig)

################################################################################
#
# PRÁCTICA 3
#
################################################################################

rank = []

@app.route('/principal', methods=['GET', 'POST'])
def pag_principal():
    if not 'urls' in session:
        session['urls'] = []

    rank = pags_visitadas()

    if request.method == 'POST':
        usuario = request.form['user']
        db = PickleShareDB('userdb')
        cad = ""

        if usuario in db.keys():
            if request.form['pss'] == db[usuario].get('pss'):
                session['user'] = usuario
                return render_template('principal.html', login=session['user'], rank=rank)

            else:
                cad = "Try again"
                return render_template('principal.html', error_login=cad, rank=rank)

    elif request.method == 'GET' and 'user' in session:
        return render_template('principal.html', login=session['user'], rank=rank)

    return render_template('principal.html', rank=rank)

@app.route('/logout', methods=['GET'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        session.pop('urls', None)


    return render_template('principal.html', rank=[])

@app.route('/about')
def pag_about():
    if 'user' in session:
        rank = pags_visitadas()
        return render_template('about.html', login=session['user'], rank=rank)

    else:
        return render_template('about.html')

@app.route('/rfa')
def pag_rfa():
    if 'user' in session:
        rank = pags_visitadas()
        return render_template('rfa.html', login=session['user'], rank=rank)

    else:
        return render_template('rfa.html')

@app.route('/goal')
def pag_goal():
    if 'user' in session:
        rank = pags_visitadas()
        return render_template('goal.html', login=session['user'], rank=rank)

    else:
        return render_template('goal.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')

@app.route('/signup', methods=['POST'])
def signup():
    rank = pags_visitadas()
    db = PickleShareDB('userdb')
    session['user'] = request.form['new_user']
    db[session['user']] = {'pss': request.form['new_pss']}
    return render_template('principal.html', login=session['user'], rank=rank)

@app.route('/modify', methods=['GET', 'POST'])
def modify():
    rank = pags_visitadas()

    if 'user' in session and not 'mod_pss' in request.form:
        return render_template('visualizar_modificar.html', login=session['user'], rank=rank)

    elif 'user' in session and 'mod_pss' in request.form:
        db = PickleShareDB('userdb')
        db[session['user']] = {'pss': request.form['mod_pss']}
        user_mod = session['user']+". Password updated"
        return render_template('principal.html', login=user_mod, rank=rank)

    else:
        return render_template('principal.html', rank=rank)

def pags_visitadas():
    if 'user' in session:
        session['urls'].append(request.url)

        if len(rank) >= 3:
            del rank[0]

        for url in session['urls']:
            pagina = re.findall(r'\/{1}\w+', url)
            if not pagina[len(pagina)-1] in rank:
                rank.append(pagina[len(paginadda)-1])

    return rank

################################################################################
#
# PRÁCTICA 4
#
################################################################################

@app.route('/mongo', methods=['GET', 'POST'])
def mongo():
    tabla = base_datos.samples_pokemon.find()

    #tabla[0]['name']
    if request.method == 'POST':
        add_to_db()

    return render_template('mongo.html', tabla=tabla)

@app.route('/add_pkm')
def add_pkm():
    return render_template('add_pkm.html')

@app.route('/modify_pkm')
def modify_pkm():
    identify = request.form['name_pk']

    if identify is not None:
        pokemon = base_datos.samples_pokemon.find_one({"name": identify})

        


@app.route('/delete_pkm', methods=['GET', 'POST'])
def delete_pkm():
    identify = request.form['name_pk']

    if identify is not None:
        base_datos.samples_pokemon.delete_one({"name": identify})

    return redirect(url_for('mongo'))

def add_to_db():
    number = request.form['no_pk']
    name = request.form['name_pk']
    image = request.form['img_pk']
    type = request.form['type_pk']
    weak = request.form['wkns_pk']

    if number is not None and name is not None and image is not None and type is not None and weak is not None:
        nuevo = {"num": number, "name": name, "img": image, "type": type, "weaknesses": weak}
        base_datos.samples_pokemon.insert_one(nuevo)

    return render_template('mongo.html')
