asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
repetir = []
for asignatura in asignaturas:
    nota = float(input(f"Nota que has sacado en {asignatura}: "))
    if nota < 5:
        repetir.append(asignatura)

print("Tienes que repetir:", repetir)