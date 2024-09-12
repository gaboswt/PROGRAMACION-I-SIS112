import funcUNID
def menu():
    print("-CONVERSOR DE UNIDADES-")
    print(" ")
    print("1) Longitud")
    print("2) Masa")
    print("3) Temperatura")
    print("4) Salir")
    print(" ")

def main():
    while True:
        menu()
        eleccion = funcUNID.opcion()
        
        if eleccion == 1:
            funcUNID.longitud()
        elif eleccion == 2:
            funcUNID.masa()
        elif eleccion == 3:
            funcUNID.temperatura()
        elif eleccion == 4:
            print("Saliendo del programa.")
            break

main()