def burbuja(lista):
    n = len(lista)
    #recorre toda la lista
    for i in range(n):
        # ultimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            #Intercambia si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista
#ejemplos de uso
lista = [5, 3, 8, 4, 2, 1]
print("Lista original:", lista)
lista_ord = burbuja(lista)
print("Lista ordenada", lista_ord)