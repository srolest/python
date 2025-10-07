#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a
#intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa
#que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el
#programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
 # Pedimos al usuario la cantidad inicial depositada
deposito = float(input("Introduce la cantidad de dinero depositada: "))

interes = 0.04

año1 = round(deposito * (1 + interes), 2)
año2 = round(año1 * (1 + interes), 2)
año3 = round(año2 * (1 + interes), 2)

print("Después del primer año:", año1,"€")
print("Después del segundo año:", año2,"€")
print("Después del tercer año:", año3,"€")
