#Los tramos impositivos para la declaración de la renta en un determinado país son
#los siguientes:
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
#el tipo impositivo que le corresponde.
renta = float(input("Introduce tu renta anual: "))

if renta < 10000:
    print("Tu impositivo es 5%")
elif 10000 <= renta < 20000:
    print("Tu impositivo es 15%")
elif 20000 <= renta < 35000:
    print("Tu impositivo es 20%")
elif 35000 <= renta < 60000:
    print("Tu impositivo es 30%")
else:
    print("Tu impositivo es 45%")