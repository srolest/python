#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.
cantidad = float(input("Introduce una cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
numerodeaños = int(input("Número de años: "))
for i in range(1, numerodeaños + 1):
    cantidad = cantidad * 1 + interes / 100
    print(f"Año {i}: capital = {cantidad:.2f}€")