# Pedimos al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Pedimos al usuario que introduzca una vocal
vocal = input("Introduce una vocal: ")


# Verificamos que la entrada sea una sola vocal
while len(vocal) != 1 or vocal.lower() not in "aeiou":
    print("Error: Debes introducir una sola vocal (a, e, i, o, u).")
    vocal = input("Introduce una vocal: ")


# Reemplazamos todas las apariciones de la vocal por su versión en mayúscula
frase_modificada = frase.replace(vocal.lower(), vocal.upper())
print("Frase modificada:", frase_modificada)
