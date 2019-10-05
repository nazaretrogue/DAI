from flask import Flask, render_template
from flask import request, abort
from PIL import Image, ImageDraw
import os, sys
import random
app = Flask(__name__)

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
    colores=['red', 'green', 'blue', 'black', 'orange']

    forma = random.choice(figuras)
    color = random.choice(colores)
    color_relleno = random.choice(colores)

    fig='<'+forma

    if forma=='circle':
        cx = random.randint(50, 200)
        cy = random.randint(50, 200)
        r = random.randint(30, 80)
        fig=fig+' cx="'+str(cx)+'" cy="'+str(cy)+'" r="'+str(r)+'"'

    elif forma=='rect':
        x = random.randint(10, 150)
        y = random.randint(10, 150)
        width = random.randint(50, 200)
        height = random.randint(50, 200)
        fig=fig+' x="'+str(x)+'" y="'+str(y)+'" width="'+str(width)+'" height="'+str(height)+'"'

    fig=fig+' stroke="'+color+'" stroke-width="4" fill="'+color_relleno+'"/>'

    return render_template('mostrar_svg.html', figura=fig)
