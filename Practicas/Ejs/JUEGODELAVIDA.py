import random
l = int(input("Introduce un numerico: "))

c = ""

for i in range(l):
    r = random.randint(1,10)

    if r <= 5:
        c += '('
    else:
        c += ')'

print("CADENICA: ",c)
