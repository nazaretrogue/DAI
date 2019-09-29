def calculaFibonacci(i):
    if i <= 1:
        return i

    else:
        return calculaFibonacci(i-1) + calculaFibonacci(i-2)

numero = open("entero_fibonacci.txt", "r")
num_leido = int(numero.read())
numero.close()

fichero_salida = open("numero_sucesion.txt", "w")
fichero_salida.write(str(calculaFibonacci(num_leido)))
fichero_salida.close()
