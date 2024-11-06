def descomponer_numero(n):
    # Caso base: si n tiene solo un dígito
    if n < 10:
        return [n]  # Devolvemos una lista con el único dígito
    
    # Caso recursivo: llamamos a la función con n // 10 para ir "dividiendo" el número
    lista_digitos = descomponer_numero(n // 10)  # Llamada recursiva
    lista_digitos.append(n % 10)  # Agregamos el último dígito al resultado de la recursión
    
    return lista_digitos

while True:
    print(" ")
    print("-DESCOMPONE TU NÚMERO-")
    x = int(input("Ingresa un número: "))
    resultado = descomponer_numero(x)
    print("Tu número descompuesto es: ", resultado)
    print(" ")
    print("¿Quieres continuar?")
    print("1.- Si")
    print("2.- No")
    op = int(input("-> "))
    if op == 2:
        print("Saliendo del sistema...")
        break