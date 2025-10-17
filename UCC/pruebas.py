texto = "Hola mundo     que tal"
print(texto)
texto = "".join(texto.split())  # Elimino los espacios
print(texto)

# [::] → toda la cadena, paso 1
print(texto[::])    # Hola mundo

# [::2] → cada 2 caracteres, empezando desde el 0
print(texto[::3])   # Hlmno etl

# [1::2] → cada 2 caracteres, empezando desde el 1
print(texto[1::2])  # o udq al

# [::-1] → toda la cadena al revés
print(texto[::-1])  # lat euq odnum aloH
