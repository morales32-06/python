# Ejercicio 12: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = int(input("Ingrese un numero entero positovo: "))

conta = 1

while(conta <= num):
      if conta % 2 != 0:
          print(conta,end=",")
      conta += 1


'''
numero = int(input("Ingresar un número: "))

if numero > 0:
    # ciclo while
    c = 1
    while(c <= numero):
        if c % 2 != 0:
            print(c, end=", ")
        c += 1
    print("------")
    # ciclo for 
    for c in range(1, numero+1):
        if c % 2 != 0:
            print(c, end=", ")
else:
    print("Ingresa un número que sea mayor que cero.")
'''



