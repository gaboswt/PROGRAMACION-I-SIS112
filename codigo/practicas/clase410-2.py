import clase410 as c
import time
listaNum=[]
listComp=int(input("Ingrese la cantidad de datos para la lista: "))
minAL=int(input("Ingrese la cantidad mínima para generar los números aleatorios: "))
maxAL=int(input("Ingrese la cantidad máxima para generar los números aleatorios: "))

inicio= time.time()
c.genlista(listComp,minAL,maxAL, listaNum)
fin=time.time()
print(f"Tiempor transcurrido de la generación de la lista \n {(fin-inicio)/1000} ms")

print(listaNum)
print(len(listaNum))
print(type(listaNum))

numENC=int(input("Ingrese el número a encotrar: "))
c.encNum(listaNum, numENC)

x=sorted(listaNum)
print(x)