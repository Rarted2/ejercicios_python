cadena = input("Introduce una cadena de caracteres (por ejemplo, 'spiderman'): ")
# Si el usuario no introduce nada, se usa "spiderman" por defecto
if not cadena:
    cadena = "spiderman"

# Definimos el alfabeto en minúsculas
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Recorremos cada letra de la cadena introducida
for letra in cadena.lower():
    # Comprobamos si la letra está en el alfabeto
    if letra in alfabeto:
        print(f"{letra}\t{alfabeto.index(letra) + 1}")
    # Si la letra no está en el alfabeto, indicamos que no es válido
    else:
        print(f"{letra}\tNo es válido")