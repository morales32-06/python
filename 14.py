# Ejercicio 14: Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo.
'''
*
**
***
****
*****
'''
num = int(input("Ingrese un numero: "))
tri = "*"
conta = 1

while( conta <= num):
    print(tri)
    tri += "*"
    conta += 1

'''
numero = int(input("Ingresar número: "))

triangulo = "*"
c = 0
while(c < numero):
    print(triangulo)
    triangulo += "*"
    c += 1
print(" ----------- ")

triangulo = "*"
for repeticion in range(numero):
    print(triangulo)
    triangulo += "*"
'''