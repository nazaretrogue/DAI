# Adivinar un número generado al azar entre 1 y 100

import random

a_adivinar = random.randint(0, 100)
num_intentos = 0
print(a_adivinar)

num_introducido = 0

while num_introducido != a_adivinar and num_intentos <10 :
    num_introducido = int(input("Adivina el número: "))

    if num_introducido == a_adivinar:
        print("Enhorabuena cruck")

    elif num_introducido > a_adivinar:
        print("El número a adivinar es menor")

    else:
        print("El número a adivinar es mayor")

    num_intentos += 1

    if num_intentos == 10:
        print("Tas pasao pringao")
