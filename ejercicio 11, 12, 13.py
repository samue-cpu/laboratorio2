#ejercicio 11
print("calcularemos su indice masa corporal para ello ingresa su peso y altura:")
peso = int(input("ingres su peso:  "))
altura =float(input("ingresa su altura: "))
IMC = peso/altura**2
if IMC < 19:
    print("tienes bajo peso")
elif  18<= IMC < 25:
    print(" tienes peso normal saludable")
elif 25<= IMC < 30 :
    print("tienes sobrepeso")
elif IMC>=30:
    print("tienes obesidad")
else:
    print("para dar IMC ingresa bien su peso y altura")
    
#ejercicio 12
numero = int(input("Ingresa un número del 1 al 7: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("erro al ingresar el numero.")
    
#ejercicio 13

edad = int(input("ingresa tu edad:"))
if edad>=18:
    print("eres mayor de edad")
else:
    print("es menor de edad")