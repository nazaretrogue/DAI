from flask import Flask, render_template
from flask import request, abort
from PIL import Image, ImageDraw
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

@app.route('/mandelbrot')
def mandelbrot():
    return render_template('mandelbrot.html')

@app.route('/imagenmandelbrot')
def imagen_mandelbrot():
    calcula_imagen(request.args.get('x1'), request.args.get('y1'), request.args.get('x2'), request.args.get('y2'))
    cad = 'src=/static/img_mdb.png alt="Imagen del fractal"'
    return render_template('mostrar_mandelbrot.html', imagen=cad)

@app.errorhandler(404)
def error_404(error):
    return "Error 404, page not found", 404

def mandelbrot(c):
    z = 0
    n = 0

    while abs(z) <= 2 and n < 100:
        z = z*z + c
        n += 1

    return n

def calcula_imagen(x1s, y1s, x2s, y2s):
    RE_START = -2
    RE_END = 1
    IM_START = -1
    IM_END = 1

    x1 = int(x1s)
    y1 = int(y1s)
    x2 = int(x2s)
    y2 = int(y2s)

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

    ANCHO = mayor_x - menor_x
    ALTO = mayor_y - menor_y
    img = Image.new('RGB', (ANCHO, ALTO), (0,0,0))
    mdb = ImageDraw.Draw(img)

    for i in range(menor_x, mayor_x):
        for j in range(menor_y, mayor_y):
            complejo = complex(RE_START+(i/ANCHO)*(RE_END-RE_START), IM_START+(j/ALTO)*(IM_END-IM_START))

            m = mandelbrot(complejo)
            color = 255 - int(m*255/100)
            mdb.point([i,j], (color,color,color))

    img.save('static/img_mdb.png')
