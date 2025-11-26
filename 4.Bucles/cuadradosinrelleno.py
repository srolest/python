n = int(input("Ingresa el tamaño del lado del cuadrado: "))

for i in range(1, n + 1):  # Bucle para las filas
    for j in range(1, n + 1):  # Bucle para las columnas
        # Imprime asterisco si es la primera o última fila/columna
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            # Imprime espacio para el interior del cuadrado
            print(" ", end=" ")
    print()  # Salto de línea al final de cada fila