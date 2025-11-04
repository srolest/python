#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable sin
#tener en cuenta mayúsculas y minúsculas.
contraseña = "SERAFIN"
variable = contraseña
preguntarcontraseña = input("Introduce la contraseña: ")
if contraseña==variable:
    print ("La contraseña es igual")
else:
    print ("La contraseña es diferente")