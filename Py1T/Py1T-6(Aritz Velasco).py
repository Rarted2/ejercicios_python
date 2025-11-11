# Lista de asignaturas
asignaturas = ["SIRL", "SIDH", "IOT", "STFM", "SPA", "DIGI"]

# Ordenar alfabéticamente
asignaturas_ordenadas = sorted(asignaturas)

# Mostrar la lista ordenada
print("Lista ordenada alfabéticamente:")
print(asignaturas_ordenadas)

# Mostrar las asignaturas en el orden original, una por línea
print("\nAsignaturas en el orden original:")
for asignatura in asignaturas:
	print(asignatura)

# Mostrar las asignaturas ordenadas en una sola línea, separadas por comas
print("\nAsignaturas ordenadas alfabéticamente en una línea:")
print(", ".join(asignaturas_ordenadas))

