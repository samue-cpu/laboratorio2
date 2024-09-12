# ejercicio 7
precio1=int(input("ingresa el precio orginal:"))
print("haciendo el descuento cada uno de los clientes,10%,15%,5%,0%")
descuento1 = precio1 - (precio1*10/100)
descuento2 = precio1 - (precio1*15/100)
descuento3 = precio1 - (precio1*5/100)
descuento4 = precio1 - (precio1*0/100)
print("el descuento a los estudiantes, jubilados,empleados, otros es:")
print(f"{descuento1} soles a estudiantes")
print(f"{descuento2} soles a jubilados")
print(f"{descuento3} soles a empleados")
print(f"{descuento4} soles a otros")
 
#ejercicio 8

numero = int(input("ingresa el numero para comprobar si es positivo o no:"))
if numero>0:
    print("es positivo")
elif numero<0:
    print("es negativo")
elif numero ==0:
    print(" es cero")
else:
    print("error al ingresar el numero")