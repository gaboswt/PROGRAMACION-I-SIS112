import PRACfunciones as func

def Main():
    while True: 
        print(" ")
        print("MENU PRINCIPAL")
        print("------------------")
        print("1.- Ingresar lista manual ")
        print("2.- Generar lista aleatoria")
        print("3.- Ordenar lista ")
        print("4.- Busqueda lineal ")
        print("5.- Busqueda binaria ")
        print("6.- Salir ")
        print(" ")

        op = int(input("Elige una opción: "))

        if op ==1:
            print(" ")
            print("-INGRESAR LISTA MANUAL-")
            print(" ")
            func.ingresar_lista()
        elif op == 2:
            print(" ")
            print("-INGRESAR LISTA ALEATORIA-")
            print(" ")
            func.generar_lista_aleatoria()
        elif op == 3:
            print(" ")
            print("-ORDENAR LISTA-")
            print(" ")
            func.ordenar_lista()
        elif op == 4:
            print(" ")
            print("-BUSQUEDA LINEAL-")
            print(" ")
            func.busqueda_lineal()
        elif op == 5:
            print(" ")
            print("-BUSQUEDA BINARIA-")
            print(" ")
            print("Para realizar este proceso, la lista seleccionada debe estar ordenada")
            print("Si no está ordenada, puede elegir ordenar la lista antes de proceder.")
            print("¿La lista está ordenada?")
            print("1.- Sí, mis listas están ordenadas")
            print("2.- No, quiero ordenar mi lista")
            print(" ")

            while True:
                opi = int(input("-> "))
                if opi == 1:
                    print(" ")
                    print("-BUSQUEDA BINARIA-")
                    print(" ")
                    func.busqueda_binaria()
                    break
                elif opi == 2:
                    print(" ")
                    print("-ORDENANDO LISTA-")
                    print(" ")
                    func.ordenar_lista()  # Esto ordenará la lista y luego vuelve al menú principal
                    func.busqueda_binaria()  # Llamamos la función después de ordenar para hacer la búsqueda
                    break
                else:
                    print("-Opción no válida, porfavor elige 1 o 2.-")
            
        elif op == 6:
            print(" ")
            print("Salienda del sistema...")
            break
        else:
            print("Opción no válida")

Main()