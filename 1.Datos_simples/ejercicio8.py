#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c>
# y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la
# división entera respectivamente.
numero1 = float(input ("Introduce un número:"))
numero2 = float(input ("Introduce un número:"))
c = numero1//numero2
r = numero1%numero2

print (numero1,"entre",numero2,"da un cociente de",c,"y un resto de",r)