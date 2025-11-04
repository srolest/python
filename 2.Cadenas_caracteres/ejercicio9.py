#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
# anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
Fechanac=input("Escribe tu fecha de nacimiento en formato dd/mm/aaaa:")
print("Tu dia de nacimiento es:"+Fechanac.split("/")[0])
print("Tu mes de nacimiento es:"+Fechanac.split("/")[1])
print("Tu año de nacimiento es:"+Fechanac.split("/")[2])