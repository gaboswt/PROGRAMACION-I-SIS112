print("-CONVERSOR DE UNIDADES-")
print(" ")
print("1) Longitud")
print("2) Masa")
print("3) Temperatura")
print(" ")

elec = int(input("Ingresa una opción del 1 al 3: "))
while True:
    if elec > 3 or elec < 1:
        print("Ingrese una opción válida")
        elec = int(input("Ingresa una opción del 1 al 3: "))
    else:
        break

if elec == 1:
    print("1) Metros a Kilómetros")
    print("2) Kilómetros a Metros")
    op1 = int(input("-> "))
    while True:
        if op1 > 2 or op1 < 1:
            print("Ingrese una opción válida")
            op1 = int(input("-> "))
        else:
            break
    if op1 == 1:
        print("Metros a Kilómetros")
        dat1 = int(input("Valor en Metros: "))
        res1 = dat1 / 1000
        print(f"Son {res1} Km")
    elif op1 == 2:
        print("Kilómetros a Metros")
        dat2 = int(input("Valor en Kilómetros: "))
        res2 = dat2 * 1000
        print(f"Son {res2} m")

elif elec == 2:
    print("1) Gramos a Kilogramos")
    print("2) Kilogramos a Gramos")
    op2 = int(input("-> "))
    while True:
        if op2 > 2 or op2 < 1:
            print("Ingrese una opción válida")
            op2 = int(input("-> "))
        else:
            break
    if op2 == 1:
        print("Gramos a Kilogramos")
        dat1 = int(input("Valor en Gramos: "))
        res1 = dat1 / 1000
        print(f"Son {res1} Kg")
    elif op2 == 2:
        print("Kilogramos a Gramos")
        dat2 = int(input("Valor en Kilogramos: "))
        res2 = dat2 * 1000
        print(f"Son {res2} g")

elif elec == 3:
    print("1) Celsius a Fahrenheit")
    print("2) Fahrenheit a Celsius")
    op3 = int(input("-> "))
    while True:
        if op3 > 2 or op3 < 1:
            print("Ingrese una opción válida")
            op3 = int(input("-> "))
        else:
            break
    if op3 == 1:
        print("Celsius a Fahrenheit")
        dat1 = int(input("Valor en Celsius: "))
        res1 = (dat1 * 9/5) + 32
        print(f"Son {res1} °F")
    elif op3 == 2:
        print("Fahrenheit a Celsius")
        dat2 = int(input("Valor en Fahrenheit: "))
        res2 = (dat2 - 32) * 5/9
        print(f"Son {res2} °C")