# Ejercicio 6: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

nombre= input("Ingrese su nombre: ")
horas= int(input("Ingrese las horas trabajadas: "))
costo= float(input("ingrese el sueldo por hora: "))

salario= horas * costo
print(f"El trabajador {nombre} trabajo {horas} horas y gano ${salario} pesos")