#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un
#programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el
#precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
# Precio habitual de una barra de pan
preciohabitual = 3.49
descuento = 0.60
barrasnofrescas = int(input("Introduce el número de barras no frescas: "))
preciodescuento = preciohabitual * descuento
costetotal = barrasnofrescas * (preciohabitual - preciodescuento)
print("Precio habitual de una barra:", preciohabitual,"€")
print("Descuento por no ser fresca:", preciodescuento,"€")
print("Coste total de",barrasnofrescas,"barras:", round(costetotal,2),"€")
