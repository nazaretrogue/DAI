import re

def correo(cadena):
    valido = re.search('.+@\w+\.\w+', cadena)
    return valido

def tarjeta(numero):
    valido = re.search('\d{4}-|\s\d{4}-|\s\d{4}-|\s\d{4}', numero)
    return valido

def nombre(cadena):
    valido = re.search('\w+\s\w', cadena)
    return valido

cadena = input("Introduce el correo: ")
numero = input("Introduce la tarjeta: ")
nom = input("Introduce tu  nombre: ")

if(correo(cadena)):
    print("Todo bien")

if(tarjeta(numero)):
    print("Tarjeta válida")

if(nombre(nom)):
    print("Nombre correcto")
