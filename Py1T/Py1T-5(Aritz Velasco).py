# Pedimos al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Pedimos al usuario que introduzca una vocal
vocal = input("Introduce una vocal: ")

# Verificamos que la entrada sea una sola vocal
while len(vocal) != 1 or vocal.lower() not in "aeiou":
    print("Error: Debes introducir una sola vocal (a, e, i, o, u).")
    vocal = input("Introduce una vocal: ")

for letra in "aeiou":
    frase = frase.replace(letra.lower(), vocal.upper()) # Reemplazamos la vocal en minúscula por la vocal nueva en mayúscula
    frase = frase.replace(letra.upper(), vocal.upper()) # Reemplazamos la vocal en mayúscula por la vocal nueva en mayúscula

print("Frase modificada:", frase)
