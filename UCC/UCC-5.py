# Programa para contar el número de letras mayúsculas en una frase

# Solicitar la frase al usuario
frase = input("Introduce una frase: ")

# Inicializar un contador para las letras mayúsculas
contador_mayusculas = 0

# Recorrer cada carácter de la frase
for caracter in frase:
    # Comprobar si el carácter es una letra mayúscula
    if caracter.isupper():
        contador_mayusculas += 1

# Mostrar el resultado
print(f"La frase contiene {contador_mayusculas} letras mayúsculas.")
