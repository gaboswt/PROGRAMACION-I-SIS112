matriz = [
    [],
    [],
    []
]
mT = [
    [],
    [],
    []
]
def ingresar_matriz():
    for i in range(3):
        for j in range(3):
            x=int(input(f"Ingresa el valor para la posición [{i}][{j}]: "))
            matriz[i].append(x)

def mostrar_matriz(matriz):
    print("\nMatriz ingresada")
    for i in matriz:
        print(" ".join(map(str, i)))

def calcular_transpuesta(matriz, mT):
    for i in range(3):
        for j in range(3):
            mT[j].append(matriz[i][j])

def mostrar_trans(mT):
    print("\nMatriz transpuesta")
    for i in mT:
        print(" ".join(map(str, i)))

def main():
    ingresar_matriz()
    mostrar_matriz(matriz)
    calcular_transpuesta(matriz, mT)
    mostrar_trans(mT)

main()