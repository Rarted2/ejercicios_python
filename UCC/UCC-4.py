# Programa para encriptar una frase según el método descrito

# Solicitar la frase al usuario
frase = input("Introduce una frase: ")

# Tomar caracteres uno sí y uno no (índices pares)
primera_parte = frase[::2]

# Tomar caracteres uno no y uno sí (índices impares)
segunda_parte = frase[1::2]

# Concatenar ambas partes
cadena_codificada = frase[::2] + frase[1::2]


# Mostrar el resultado
print("Frase encriptada:", cadena_codificada[::-1])