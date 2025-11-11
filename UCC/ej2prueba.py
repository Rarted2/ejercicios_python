texto = input("Ingrese un texto: ")
texto_formateado = texto.replace(" ", "").lower()
texto_invertido = texto_formateado[::-1]

if texto_formateado == texto_invertido:
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")