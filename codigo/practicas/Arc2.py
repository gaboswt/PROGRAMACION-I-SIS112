import random
import time

lista_Manual = []
lista_Ale= []

def ingresar_lista():
    n= int(input("Ingresa el tamño de la lista: "))
    for i in range(n): #Permite ingresar digitos "n" veces
        while True:
            x = int(input("Ingrese un número: "))
            print(" ")
            if x in lista_Manual: #Valida si el dígito ingresado ya está en la lista
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
            if z not in lista_Ale: #Valida si el dígito generado ya está en la lista
                lista_Ale.append(z)
                print(f"-Número {z} agregado correctamente")
                break

def busqueda_lineal():
    print("-Seleccione la lista en la cual buscar-")
    print("1.- Lista Manual ")
    print("2.- Lista Aleatoria")
    while True:
        op = int(input("-> "))
        if op == 1: #Valida cual de las dos lista se va a utilizar
            print("-Lista Manual seleccionada-")
            print(" ")
            x = int(input("Ingrese el número a buscar: "))
            print(" ")
            indice = -1 #Asignando un valor, para validar despues si es que el dígito está en la lista
            ini = time.time()
            for i in range(len(lista_Manual)):
                if lista_Manual[i] == x:
                    indice = i
                    break
            fin = time.time()
            if indice != -1:
                print(f"El número {x} se encontró en la posición {indice} de la lista")
                break
            else:
                print("El número no se encuentra en la lista")
                break

        elif op == 2:
            print("-Lista Aleatoria seleccionada-")
            print(" ")
            x = int(input("Ingrese el número a buscar: "))
            print(" ")
            indice = -1 #Asignando un valor, para validar despues si es que el dígito está en la lista
            ini = time.time()
            for i in range(len(lista_Ale)):
                if lista_Ale[i] == x:
                    indice = i
                    break
            fin = time.time()
            if indice != -1:
                print(f"El número {x} se encontró en la posición {indice} de la lista")
                print(" ")
                break
            else:
                print("El número no se encuentra en la lista")
                print(" ")
                break  

        else:
            print("Opción no válida")
            print(" ")
    print(f"Tiempo transcurrido de la busqueda del número es de \n {(fin-ini)/1000} ms")

def busqueda_binaria_lista(lista, numero): #código de busqueda binaria
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

def busqueda_binaria():
    print(" ")
    print("-Seleccione la lista en la cual buscar-")
    print("1.- Lista Manual ")
    print("2.- Lista Aleatoria ")
    while True:
        op = int(input("-> "))
        if op == 1:
            print("-Lista Manual seleccionada-")
            x = int(input("Ingrese el número a buscar: "))
            ini = time.time()
            indice = busqueda_binaria_lista(lista_Manual, x) #Se llama a la función de busqueda binaria para reducir el código
            fin = time.time()
            if indice != -1:
                print()
                print(f"El número {x} se encontró en la posición {indice} de la lista Manual")
                break
            else:
                print("El número no está en la lista Manual")
            break
        elif op == 2:
            print("-Lista Aleatoria seleccionada-")
            x = int(input("Ingrese el número a buscar: "))
            ini = time.time()
            indice = busqueda_binaria_lista(lista_Ale, x) #Se llama a la función de busqueda binaria para reducir el código
            fin = time.time()
            if indice != -1:
                print(f"El número {x} se encontró en la posición {indice} de la lista Aleatoria")
                break
            else:
                print("El número no está en la lista Aleatoria")
            break
        else:
            print("Opción no válida")
    print(f"Tiempo transcurrido de la busqueda del número es de \n {(fin-ini)/1000} ms")

def burbuja(lista): #Código del ordenamiento burbuja
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_lista(): #Función para ordenar la lista antes de usar la buqueda binaria
    print("-Seleccione la lista a ordenar-")
    print("1.- Lista Manual ")
    print("2.- Lista Aleatoria ")
    while True:
        op = int(input("-> "))
        if op == 1: #Valida cual de las dos lista se va a utilizar
            print("Lista Manual", lista_Manual)
            ini = time.time()
            burbuja(lista_Manual) #Se llama a la función de ordenamiento burbuja
            fin = time.time()
            print("Lista Manual ordenada:", lista_Manual)
            break
        elif op == 2:
            print("Lista Aleatoria", lista_Ale)
            ini = time.time()
            burbuja(lista_Ale) #Se llama a la función de ordenamiento burbuja
            fin = time.time()
            print("Lista Aleatoria ordenada:", lista_Ale)
            break
        else:
            print("Opción no válida")
    print(" ")
    print(f"Tiempo transcurrido del ordenamiento del número es de \n {(fin-ini)/1000} ms")

def descomponer_numero(n):
    #Si n tiene solo un dígito
    if n < 10:
        return [n]  
    
    #Llamamos a la función con n // 10 para ir "dividiendo" el número
    lista_digitos = descomponer_numero(n // 10)  
    lista_digitos.append(n % 10)  #Se agrega el último dígito
    
    return lista_digitos
