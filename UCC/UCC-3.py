cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

cadena_conjunta = ""

for i in range(4):
    cadena_conjunta += cadena1 + " "


for i in range(6):
    cadena_conjunta += cadena2 + " "


print("Cadena conjunta: " + cadena_conjunta.strip())