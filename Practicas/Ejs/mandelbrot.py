from PIL import Image, ImageDraw

def mandelbrot(c):
    z = 0
    n = 0

    while abs(z) <= 2 and n < 100:
        z = z*z + c
        n += 1

    return n

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

x1 = int(input("Introduce la coordenada x1: "))
y1 = int(input("Introduce la coordenada y1: "))
x2 = int(input("Introduce la coordenada x2: "))
y2 = int(input("Introduce la coordenada y2: "))
ANCHO = 1024
ALTO = 750

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

img.save('imagen_mandelbrot.png')
