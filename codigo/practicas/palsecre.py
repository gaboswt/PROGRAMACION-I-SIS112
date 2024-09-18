import random
lista=["hola", "adios", "progra", "ucb", "biomedica"]
palsec = random.choice(lista)
intentos = 10
palnoencontrada = ["_"] * len(palsec)
print("".join(palnoencontrada))
for i in range (intentos):
    new = input("Ingresa letra: ")
    for j in range(len(palsec)):
        if new == palsec[j]:
            palnoencontrada[j]=new
    print("".join(palnoencontrada))
    if "_" not in palnoencontrada:
        print("¡FELCIDADES, encontraste la palabra!")
else:
    print(f"Te quedaste sin intentos. La palabra era: {palsec}")