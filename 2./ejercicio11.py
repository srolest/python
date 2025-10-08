#Escribir un programa que pregunte el nombre el un producto, su precio y un número
# de unidades y muestre por pantalla una cadena con el nombre del producto seguido
# de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
# tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))
costetotal=precio*unidades
print(f"El nombre del producto es {producto}, su precio unitario es {precio:09.2f}, "
      f"el número de unidades es {unidades:03d} y el coste total es {costetotal:08.2f}")