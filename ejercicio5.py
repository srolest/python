#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
Numhoras = float(input("Ingresa el número de horas:"))
Costehoras = float(input("Ingresa el coste por horas:"))
print ("Te corresponde",Numhoras*Costehoras,"€")