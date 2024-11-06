m_1 = [
    [],
    [],
    []
]
m_2 = [
    [],
    [],
    []
]

def ingresar_matriz_1():
    print("--Matriz 1--")
    for i in range(3):
        for j in range(3):
            x=int(input(f"Ingresa el valor para la posición [{i}][{j}]: "))
            m_1[i].append(x)

def mostrar_matriz1(m_1):
    print("\nMatriz 1 ingresada")
    for i in m_1:
        print(" ".join(map(str, i)))

def ingresar_matriz_2():
    print("--Matriz 2--")
    for i in range(3):
        for j in range(3):
            x=int(input(f"Ingresa el valor para la posición [{i}][{j}]: "))
            m_2[i].append(x)

def mostrar_matriz2(m_2):
    print("\nMatriz 2 ingresada")
    for i in m_2:
        print(" ".join(map(str, i)))

def multiplicar_matrices(m_1, m_2):
    resultado = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in range(3):  # Recorre las filas de la matriz 1
        for j in range(3):  # Recorre las columnas de la matriz 2
            for k in range(3):  # Variable que recorre para multiplicar y sumar
                resultado[i][j] += m_1[i][k] * m_2[k][j]

    print("\nMatriz resultante de la multiplicación:")
    for i in resultado:
        print(" ".join(map(str, i)))

def main():
    ingresar_matriz_1()
    ingresar_matriz_2()
    mostrar_matriz1(m_1)
    mostrar_matriz2(m_2)
    multiplicar_matrices(m_1, m_2)

main()