#   Inicializo el valor minimo con un valor muy alto para que el primer valor lo resetee 
#   Inicializo el valor maximo con la misma mentalidad que el minimo, pero al revés
valor_min = 99999999999999999999999999999999
valor_max = 0
media = 0
valor_in = 0

for i in range(10): 
    #	Utilizo print(f””) para poder utilizar variables directamente en el texto que se imprima, y sumo 1 porque empieza a contar desde el 0
    valor_in = int(input(f"Introduzca el dato del coche {i + 1}: "))
    while valor_in <= 0:    
        #   Trampa para que el valor que introduzca el usuario no sea negativo ni nulo
        valor_in = int(input(f"Introduzca correctamente el dato del coche {i + 1}: "))
    #   Compruebo si el valor introducido es menor que el minimo o mayor que el maximo
    if valor_in < valor_min:
        valor_min = valor_in
    if valor_in > valor_max:
        valor_max = valor_in
    media += valor_in

print("---------------------------------------") 
#   Hago un salto de línea por comodidad visual
print(f"El valor mínimo es {valor_min} y el valor máximo es {valor_max}")
print("---------------------------------------") 
#   Hago un salto de línea por comodidad visual
print(f"El índice contaminante promedio detectado es: {media / 10}")
print("---------------------------------------") 
