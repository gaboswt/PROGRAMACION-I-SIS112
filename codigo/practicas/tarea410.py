#hacer busqueda binaria 
import random
import time
lista = []
for i in range (100):
    x = random.randint(1, 100)
    lista.append(x)

lista.sort()
print("Lista ordenada:")
print(lista)

numero = int(input("Ingresa el número a buscar: "))   
def busq_bin(lista, numero):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista [medio] == numero:
            return medio
        elif lista [medio] <  numero:
            izquierda = medio + 1
        else: 
            derecha = medio -1
    return -1
ini =time.time()
indice = busq_bin(lista, numero)
fin = time.time()
if indice != -1:
    print(f'El número {numero} se encuentra en el índice {indice}.')
else:
    print(f'El número {numero} no está en la lista.')

print(f"Tiempor transcurrido de la generación de la lista \n {(fin-ini)/1000} ms")

