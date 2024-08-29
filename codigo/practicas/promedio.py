n=int(input("-Ingresa la cantidad de notas a ingresar: "))
v = n
suma = 0
while n > 0:
    nota = int(input("Ingresa una nota: "))
    n-=1
    suma += nota
prom=suma/v
print(" ")
print(f"El promedio es: {prom}")