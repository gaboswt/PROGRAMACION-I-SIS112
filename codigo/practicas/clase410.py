import random

def genlista(t,vmin,vamx, lista):
    for i in range(t):
        ale=random.randint(vmin,vamx)
        lista.append(ale)
    return lista

def encNum(lista, num):
    for i in range(len(lista)):
        if(num==lista[i]):
            print(f"Número encontrado en el índice{i}: ")
            return 1
        else:
            return -1
        