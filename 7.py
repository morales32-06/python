# Ejercicio 7: Pedir el precio de un producto y calcular su IVA (21%) y su valor original

costo= float(input("ingrese el presio del producto: "))

iva= costo * 0.21
print("El IVA del producto es: {:.1f}".format(iva))
preal= costo - iva
print("El valor original es: {:.1f}".format(preal))



## Concepto matemático

#precio = int(input("Ingresar precio: "))

# iva = (precio * 21) / 100
#iva = precio * 0.21
#original = precio - iva

#print("El IVA del producto es:", iva)
#print("Y su valor original es:", original)