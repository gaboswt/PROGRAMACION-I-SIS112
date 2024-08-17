def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no es permitida."

def mostrar_menu():
    print("BIENVENIDO A LA CALCULADORA VIRTUAL :)")
    print("-------------------")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Salir")

def obtener_resultado(operacion, num1, num2):
    if operacion == 1:
        return sumar(num1, num2)
    elif operacion == 2:
        return restar(num1, num2)
    elif operacion == 3:
        return multiplicar(num1, num2)
    elif operacion == 4:
        return dividir(num1, num2)

def calculadora():
    while True:
        num1 = int(input("-Ingresa el primer número: "))
        num2 = int(input("-Ingresa el segundo número: "))

        mostrar_menu()
        oper = int(input("->"))

        if 1 <= oper <= 4:
            resultado = obtener_resultado(oper, num1, num2)
            print(f"El resultado es: {resultado}")
        elif oper == 5:
            print("Gracias por su preferencia :)")
            break
        else:
            print("-Ingrese un valor en el rango establecido-")
        
        repetir = int(input("¿Desea realizar otra operación? (1 = sí, 2 = no): "))
        if repetir != 1:
            print("Gracias por su preferencia :)")
            break

calculadora()