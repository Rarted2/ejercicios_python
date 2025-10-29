# Añade un número introducido por el usuario al final de una tupla dada
tupla = (1,2,3,4,5)
num = int(input("Introduce un numero: "))


# Convertir la tupla a lista para poder modificarla
lista = list(tupla)
lista.append(num)
tupla = tuple(lista)


# Mostrar la tupla actualizada
print(tupla)