frase = ""
cadena_in = ""

while True:
    cadena_in = input("Introduce una cadena de caracteres (o '.' para terminar): ").strip()
    frase += cadena_in + " "
    if cadena_in == "." or cadena_in == "?" or cadena_in == "!":
        break
print("Frase completa:  " + frase.strip())