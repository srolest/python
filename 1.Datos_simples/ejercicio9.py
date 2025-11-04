#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidadivertir = float(input("Introduce la cantidad a invertir:"))
interesanual = float(input("Introduce el interes anual (en porcentaje):"))
numeroaños = float(input("Introduce el numero de años:"))
print ("El capital obtenido en la inversión es:", cantidadivertir*interesanual*numeroaños)