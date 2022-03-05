#ejemplo de estaciones


mes= input("Digite un mes del año:  ").lower()
print(f"el mes digitado fue:  {mes}")

if (mes == "diciembre" or mes =="enero" or mes =="febrero" or mes =="marzo"):
    print(f"la estación del año es Invierno")
elif (mes == "junio" or mes =="julio" or mes =="agosto"):
    print(f"la estación del año es Verano")
elif (mes == "abril" or mes =="mayo"):
    print(f"la estación del año es Primavera")
elif (mes == "septiembre" or mes =="octubre" or mes =="noviembre"):
    print(f"la estación del año es Primavera")
else: 
    print(f"Digite un mes valido")