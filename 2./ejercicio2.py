#Escribir un programa que pregunte el nombre completo del usuario en la consola y
# después muestre por pantalla el nombre completo del usuario tres veces, una con
# todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
# primera letra del nombre y de los apellidos en mayúscula. El usuario puede
# introducir su nombre combinando mayúsculas y minúsculas como quiera.
Nombrecompleto = input("Inserte su nombre completo:")
print(Nombrecompleto.title()+ "\n")
print(Nombrecompleto.lower()+ "\n")
print(Nombrecompleto.upper()+ "\n")