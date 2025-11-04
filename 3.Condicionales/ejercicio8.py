#En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
#intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
#los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
#en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Escribir un programa que lea la puntuación del usuario e indique su nivel de
#rendimiento, así como la cantidad de dinero que recibirá el usuario.
puntuacion = float(input("Introduce tu puntuación: "))
if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None

if nivel:
    dinero = 2400 * puntuacion
    print(f"Tu nivel de rendimiento es: {nivel}")
    print(f"Te corresponde una cantidad de: {dinero:.2f} €")
else:
    print("La puntuación introducida no es válida.")

