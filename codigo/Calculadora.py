print("BIENVENIDO A LA CALCULADORA VIRTUAL :)")
print("-------------------")
num1 = int(input("-Ingresa el primer número: "))
num2 = int(input("-Ingresa el segundo número: "))
print("     ")
print("--ELIJA LA OPERACIÓN A REALIZAR--")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicación")
print("4.- División")
print("5.- Salir")

while True: 
    oper = int(input("->"))
    if oper > 0 and oper < 6:
        if oper == 1:
            resultado = num1 + num2
            print("El resultado es: " + str(resultado))
        elif oper == 2:
            resultado = num1 - num2
            print("El resultado es: " + str(resultado))
        elif oper == 3:
            resultado = num1 * num2
            print("El resultado es: " + str(resultado))
        elif oper == 4:
            if num2 != 0:
                resultado = num1 / num2
                print("El resultado es: " + str(resultado))
            else:
                print("Error: División por cero no es permitida.")
        elif oper == 5:
            print("Gracias por su preferencia :)")
            break
    else:
        print("-Ingrese un valor en el rango establecido-")