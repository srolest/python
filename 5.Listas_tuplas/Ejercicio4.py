numeros= []
for i in range(6):
    num= int(input(f"Introduce el numero ganador de la primitiva {i+1}:"))
    i+1
    numeros.append(num)
numeros.sort()
print ("Los numeros ganadores son:", numeros)