#!/usr/bin/env python3

def obtener_iniciales(nombre):
    palabras = nombre.split()
    iniciales = ''.join([palabra[0].upper() for palabra in palabras if palabra])
    return iniciales

if __name__ == "__main__":
    nombre_estamento = input("Introduce el texto: ")
    print(obtener_iniciales(nombre_estamento))
