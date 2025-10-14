#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.
numero1 = int(input ("Introduce un dividendo: "))
numero2 = int(input ("Introduce el divisor: "))

if numero2==0:
    print ("Error")
else:
    print ("La division de los dos numeros es:", numero1/numero2)