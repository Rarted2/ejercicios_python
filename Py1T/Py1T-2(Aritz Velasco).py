peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el resultado redondeado a 2 decimales
print(f"Tu índice de masa corporal es {imc:.2f}")
