tope = int(input("Introduce el tope: "))

numeros = set()
primos = []

for i in range(2, tope):
    if i not in numeros:
        primos.append(i)
        numeros.update(range(i*i, tope, i))

print("Los primos entre 2 y ", tope, " son ")

for i in range(len(primos)):
    print(primos[i], end=' ')

print()
