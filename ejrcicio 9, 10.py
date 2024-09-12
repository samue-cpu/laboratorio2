#ejercicio 9
año = int(input("ingresa un años:"))
if año % 4 == 0:
    print(f"{año} es bisiesto")
elif año % 100 != 0 or (año % 400 == 0):
    print(f"{año} no es bisiesto")
else:
    print("error al ingresar el año")
    
#ejercicio 10

longitud =int(input("ingresa una longitud para convertir:"))
pies = longitud* 3.28/1
pulgada= longitud*39.37/1
yarda = longitud*1/0.914
print("la conversion de metros a pies, pulgadas, yardas es:")
print(f"{longitud}m equivale a {pies} pies")
print(f"{longitud}m equivale a {pulgada} pulgadas")
print(f"{longitud}m equivale a {yarda} yardas")