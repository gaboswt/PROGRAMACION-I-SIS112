import random
lista=["hola", "adios", "progra", "ucb", "biomedica"]

palsec = random.choice(lista)
intentos = 10
palnoencontrada = ["_"] * len(palsec)
print(palnoencontrada)

for i in range (intentos):
    new = input("Ingresa una letra: ")
    for j in range(len(palsec)):
        if new == palsec[j]:
            palnoencontrada[j]=new
    print(palnoencontrada)
    if "_" not in palnoencontrada:
        print("¡FELICIDADES, encontraste la palabra!")
else:
    print(f"Te quedaste sin intentos. La palabra era: {palsec}")