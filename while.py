#variable controladora

import math




#declarar bucle

print("empanadas el Machetico")
print("*******************************************************")
print("0 Digita 0 para salir")
print("1. digita 1 para sacar sacar raíz cuadrada")
print("2. digita 2 y un número para calcular la potencia 2 de un #")
print("********************************************************")
opcion=1

while(opcion!=0):

    opcion=int(input("digita un una opción: "))
    #preguntar opcion
    if(opcion==0):
        print("Hasta pronto")
        break
    elif(opcion==1):
        numero=int(input("digita un numero: "))
        raiz=math.sqrt(numero)
        print(f"la raiz del número {numero} es  {raiz}")
    elif(opcion==2):
        numero=int(input("digita un numero: "))
        potencia=math.pow(numero,2)
        print(f"La potencia al cuadrado de {numero} es {potencia}")
    else:
        print("Ingrese una opción valida")
        