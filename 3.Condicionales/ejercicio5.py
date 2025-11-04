#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
#ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que
#pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el
#usuario tiene que tributar o no.
edad = int(input("Introuce tu edad: "))
ingresosmensuales = int(input("Intoduce tus ingresos mensuales en euros: "))
if edad > 16 and ingresosmensuales >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")