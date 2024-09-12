#ejercicio 2

lado1 = int(input("ingresa el primer lado:"))
lado2 = int(input("ingresa el seguno lado:"))
lado3 = int(input("ingresa lado tercero:"))

if lado1==lado2==lado3:
    print("es un triangulo equilatero")
elif lado1 ==lado2 != lado3:
    print("es un triangulo isoseles")
elif lado1!=lado2!=lado3:
    print("es un triangulo escaleno")
else:
    print("error en ingresar ")
    
    #ejercicio3
notas_artmetica = "parcial1, parcial2, practica1, practica2 "
nota1 = int(input("ingrese el promedio de parcial1:"))
nota2= int(input("ingrese el promedio de parcial2:"))
nota3 = int(input("ingres el promedio de practica1:"))
nota4 =int(input("ingrese el promedio de practica2:"))
promediofinal= (nota1+ nota2+nota3+nota4)/4
print("tu nota final es:",promediofinal)

if 11<= promediofinal< 15:
    print("aprobaste el curso del semestre ")
elif promediofinal >= 15:
    print("muy buena felicidades aprobaste ")
else:
    print("desaprobaste ")
    
    #ejrcicio 4
print("hola en que le puedo ayudar")
dato1 = input("ingresa:")
print("oky aqui le ayudo ")
a =int(input("ingres el primer numero:"))
b = int(input("ingresa el segundo numero:"))

suma = a +b
resta = a-b
division= a/b
multi= a*b

if dato1 == "suma":
    print("la suma es:",suma)
elif dato1 == "resta":
    print("la resta es:", resta)
elif dato1 == "division":
    print("la division es:", division)
elif dato1 == "multi":
    print("la multi es:", multi)
else:
    print("ingresa bien el dato1")