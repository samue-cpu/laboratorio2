# ejercicio 5
numero1=int(input("introdusca una numero para comprobar:"))
if numero1%2==0:
    print("es par")
else: 
    print("es impar")
    
#ejercicio 6
numr1=int(input("ingresa el numero:"))
numr2 =int(input("ingresa el segundo numero:"))
numr3 = int(input("ingresa el tercer numero"))
print("comprobando cual es mayor:")
if numr1>numr2 :
    print(f"{numr1} es mayor que los dos")
elif numr2>numr3:
    print(f"{numr2} es mayor que los dos")
elif numr3>numr1 or numr3>numr2:
    print(f"{numr3} es mayor que los dos")
else:
    print("error al ingresar los numeros")