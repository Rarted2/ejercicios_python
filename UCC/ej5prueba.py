nombre = input("Nombre: ")
listanombre = nombre.split()
if len(listanombre) != 3:
    print("Longitud de nombre incorrecta")
else:
    usuario = listanombre[0][::2].lower() + listanombre[1][:3].lower() + listanombre[2][:3].lower()
    correo = usuario + "@unican.es"
    print(f"Usuario: {usuario}")
    print(f"Correo: {correo}")
        