import random

ale = random.randint(1, 100)

def nume(): 
    print(" ") 
    num = int(input("Introduce un número: "))
    return num
        
def valores(ale):
    veces = 0
    while True:
        num = nume()
        if num < ale:
            print("-Demasiado bajo. Intenta de nuevo.")
            veces +=1
        elif num > ale:
            print("-Demasiado alto. Intenta de nuevo.")
            veces += 1
        else: 
            veces += 1
            print(" ")
            print(f"¡FELICIDADES!, lo has adivinado en {veces} intentos.")
            break
    
def main():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 al 100. ¿Puedes adivinar cual es?")
    print(" ")
    valores(ale)

main()