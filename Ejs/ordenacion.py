import random
import time

def  burbuja(v):
    for i in range(len(v)):
        for j in range(len(v)-i-1):
            if v[j] > v[j+1]:
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux

v=[]

for i in range(10):
    num = random.randint(0,20)
    v.append(num)

print("Ordenando...")

inicio = time.time()
burbuja(v)
fin = time.time()

print("La ordenación ha tardado ", fin-inicio, " segundos")

for i in range(len(v)):
    print(v[i])
