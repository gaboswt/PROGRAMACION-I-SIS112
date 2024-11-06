import random
lista=[]
for i in range(100):
    v = random.randint(1, 100)
    if v not in lista:
        lista.append(v)

while True:
    valor = int(input("Ingresa un número dentro del rango del 1 al 100: "))
    if valor > 100 or valor < 0:
        print("Ingresa un valor válido del 1 al 100")
    else:
        break

def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

print(lista)
print(type(lista))
print(len(lista))

lis=[]
def genlist(rango, Vmax, Vmin, lis):
    for i in range(rango):
        x = random.randint(Vmax, Vmin)
        lis.append(x)
    return lis
genlist(50, 5, 50, lis)
print(lis)
print(len(lis))
