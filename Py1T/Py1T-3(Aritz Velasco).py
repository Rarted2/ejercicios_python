# Preguntar al usuario si quiere una pizza vegetariana o no
tipo = input("¿Deseas una pizza vegetariana? (si/no): ").strip().lower()

# Según el tipo, mostramos las opciones correspondientes
if tipo == "si":
    print("Ingredientes disponibles (vegetarianos):")
    print("1. Pimiento")
    print("2. Tofu")
    opcion = input("Elige un ingrediente (1 o 2): ").strip()
    while(opcion != "1" and opcion != "2"):
        opcion = input("Elige un ingrediente (1 o 2): ").strip()
    if opcion == "1":
        ingrediente = "Pimiento"
    elif opcion == "2":
        ingrediente = "Tofu"
    else:
        print("Opción no válida. Se usará Pimiento por defecto.")
        ingrediente = "Pimiento"
    tipo_pizza = "vegetariana"
else:
    print("Ingredientes disponibles (no vegetarianos):")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    opcion = input("Elige un ingrediente (1, 2 o 3): ").strip()
    while(opcion != "1" and opcion != "2" and opcion != "3"):
        opcion = input("Elige un ingrediente (1, 2 o 3): ").strip()
    if opcion == "1":
        ingrediente = "Pepperoni"
    elif opcion == "2":
        ingrediente = "Jamón"
    elif opcion == "3":
        ingrediente = "Salmón"
    else:
        print("Opción no válida. Se usará Pepperoni por defecto.")
        ingrediente = "Pepperoni"
    tipo_pizza = "no vegetariana"

# \n para crear una nueva línea, por comodidad visual
print("\nTu pizza es", tipo_pizza, "y lleva los siguientes ingredientes:")
print("- Mozzarella")
print("- Tomate")
print(f"- {ingrediente}")
