#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo
#almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice
#de masa corporal calculado redondeado con dos decimales.
altura=float(input("Introduce tu altura:"))
peso=float(input("Introduce tu peso:"))
IMC = peso/(altura**2)
print("Tu índice de masa corporal es:",IMC)