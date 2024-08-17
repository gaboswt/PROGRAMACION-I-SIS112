def Sum(a, b):
    return a + b

def rest(a,b):
    return a - b

def mult(a,b):
    return a * b

def divi(a,b):
    if b != 0:
        return a / b
    else:
        print("No existe")

def menu():
    print("BIENVENIDO A LA CALCULADORA VIRTUAL :)")
    print("-------------------")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Salir")

def selec_oper(oper, num1, num2):
    if oper == 1:
        return Sum(num1, num2)
    elif oper == 2:
        return rest(num1, num2)
    elif oper == 3:
        return mult(num1, num2)
    elif oper == 4:
        return divi(num1, num2)

def calcu():
    while True:
        num1= int(input("Ingresa el primer número: "))
        num2= int(input("Ingresa el primer número: "))
        menu()
        oper = int(input("->"))

        if oper >= 1 and oper <= 4:
            resultado = selec_oper(oper, num1, num2)
            print(f"El resultado es: {resultado}")
        elif oper == 5:
            print("Gracias por jugar :)")
            break
        else: 
            print("-Valor no válido-")

       print("¿Quieres repetir la calculadora?")
       print("Si=1, No= 2")
       repetir = int(input("->"))
       if repetir != 1:
            print("Gracias por su preferencia :)")
            break

calcu()