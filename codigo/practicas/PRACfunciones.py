import random

lista_Manual = []
lista_Ale= []

def ingresar_lista():
    while True:
        x = int(input("Ingrese un número: "))
        print(" ")
        if x in lista_Manual:
            print("El número ingresado ya está en la lista")
            print(" ")
        else:
            lista_Manual.append(x)
            print("Número agregado correctamente")
            break

def generar_lista_aleatoria():
    lista_Ale.clear() #limpiar la lista antes de generar una nueva
    y = int(input("Ingrese el tamaño de la lista: "))
    for i in range(y):
        while True:
            z = random.randint(1,100)
            if z not in lista_Ale:
                lista_Ale.append(z)
                print(f"Número {z} agregado correctamente")
                break

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_lista():
    print("-Seleccione la lista a ordenar-")
    print("1.- Lista Manual ")
    print("2.- Lista ordenada ")
    while True:
        op = int(input("-> "))
        if op == 1:
            print("Lista Manual", lista_Manual)
            burbuja(lista_Manual)
            print("Lista Manual ordenada:", lista_Manual)
            break
        elif op == 2:
            print("Lista Aleatoria", lista_Ale)
            burbuja(lista_Ale)
            print("Lista Aleatoria ordenada:", lista_Ale)
            break
        else:
            print("Opción no válida")
            

def busqueda_lineal():
    print("-Seleccione la lista en la cual buscar-")
    print("1.- Lista Manual ")
    print("2.- Lista ordenada ")
    while True:
        op = int(input("-> "))
        if op == 1:
            print("-Lista Manual seleccionada-")
            x = int(input("Ingrese el número a buscar: "))
            indice = -1
            for i in range(len(lista_Manual)):
                if lista_Manual[i] == x:
                    indice = i
                    break
            if indice != -1:
                print(f"El número {x} se encontró en la posición {indice} de la lista")
            else:
                print("El número no se encuentra en la lista")
            break

        elif op == 2:
            print("-Lista Aleatoria seleccionada-")
            x = int(input("Ingrese el número a buscar: "))
            indice = -1
            for i in range(len(lista_Ale)):
                if lista_Ale[i] == x:
                    indice = i
                    break
            if indice != -1:
                print(f"El número {x} se encontró en la posición {indice} de la lista")
            else:
                print("El número no se encuentra en la lista")
            break  

        else:
            print("Opción no válida")
            print(" ")

def busqueda_binaria():
    print("-Seleccione la lista en la cual buscar-")
    print("1.- Lista Manual ")
    print("2.- Lista ordenada ")
    while True:
        op = int(input("-> "))
        if op == 1:
            print("-Lista Manual seleccionada-")
            x = int(input("Ingrese el número a buscar: "))
            indice = busqueda_binaria_lista(lista_Manual, x)
            if indice != -1:
                print(f"El número {x} se encontró en la posición {indice} de la lista Manual")
            else:
                print("El número no está en la lista Manual")
            break
        elif op == 2:
            print("-Lista Aleatoria seleccionada-")
            x = int(input("Ingrese el número a buscar: "))
            indice = busqueda_binaria_lista(lista_Ale, x)
            if indice != -1:
                print(f"El número {x} se encontró en la posición {indice} de la lista Aleatoria")
            else:
                print("El número no está en la lista Aleatoria")
            break
        else:
            print("Opción no válida")

def busqueda_binaria_lista(lista, numero):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1