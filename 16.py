# Ejercicio 16: Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.print("Negativo:", palabra[-1])

palabra = input("Ingrese una palabra: ")
conta = len(palabra)-1
while(conta >= 0):
    print(palabra[conta])
    conta -= 1



'''
palabra = input("Ingresar palabra: ")

posicion = len(palabra)-1
while(posicion >= 0):
    print(palabra[posicion])
    posicion -= 1
print("--------------")
posicion = len(palabra)-1
for posicion in range(posicion, -1, -1):
    print(palabra[posicion])

'''