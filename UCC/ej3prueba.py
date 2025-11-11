alumnos = int(input("Cuántos alumnos son?: "))

listanotas = []

for i in range(alumnos):
    listanotas.append(float(input(f"Nota del alumno {i+1}: ")))
    
print(f"La nota más alta es: {max(listanotas):.2f}")
print(f"La nota más baja es: {min(listanotas):.2f}")
print(f"La media de las notas es: {sum(listanotas)/alumnos:.2f}")
