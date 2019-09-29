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

ANCHO = int(input("Introduce el ancho: "))
ALTO = int(input("Introduce el alto: "))


img = Image.new('RGB', (ANCHO, ALTO), (0,0,0))
mdb = ImageDraw.Draw(img)

for i in range(0, ANCHO):
    for j in range(0, ALTO):
        complejo = complex(RE_START+(i/ANCHO)*(RE_END-RE_START), IM_START+(j/ALTO)*(IM_END-IM_START))

        m = mandelbrot(complejo)
        color = 255 - int(m*255/100)
        mdb.point([i,j], (color,color,color))

img.save('imagen_mandelbrot.png')
