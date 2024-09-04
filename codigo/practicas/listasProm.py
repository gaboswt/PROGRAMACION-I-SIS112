def datos():
    notas = []
    while True:
        num = int(input("-Ingrese la cantidad de estudiantes: "))
        print(" ")
        if num > 0:
            break
        else:
            print("-Valor no válido-")
    
    for i in range(num):
        nota = int(input(f"Ingrese la nota N°{i + 1}: "))
        notas.append(nota)
    return notas

def calculo(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def mostrar(promedio, num):
    print("")
    print(f"El promedio de las {num} notas ingresadas es {promedio}")

def main():
    print("")
    print("CALCULADORA DE PROMEDIO :)")
    print(" ")
    notas = datos()
    promedio= calculo(notas)
    mostrar(promedio, len(notas))
main()