# La pizzería Il Capo ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes
# para cada tipo de pizza son:
# • Ingredientes vegetarianos: Pimiento y tofu.
# • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Implementar un programa en lenguaje Python que pregunte al usuario si quiere una pizza
# vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes
# disponibles para que elija. Sólo se puede eligir un ingrediente además de la mozzarella y el
# tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
# vegetariana o no y todos los ingredientes que lleva.



# Ingredientes base comunes a todas las pizzas
INGREDIENTES_BASE = "Mozzarella, Tomate"

# Ingredientes disponibles
VEGETARIANOS = ["Pimiento", "Tofu"]
NO_VEGETARIANOS = ["Peperoni", "Jamón", "Salmón"]

# Inicializar variables
ingrediente_extra = ""
pizza_elegida = ""


print("--- Pizzería Il Capo ---")

# Pedir tipo de pizza y convertir a minúsculas para facilitar la comparación
tipo_pizza = input("¿Quiere una pizza Vegetariana (V) o No Vegetariana (N)? ").lower()


if tipo_pizza == 'v':
    pizza_elegida = "Vegetariana"
    
    # Mostrar opciones vegetarianas
    print("\nIngredientes vegetarianos disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
    
    opcion = input("Elija un ingrediente extra (1 o 2): ")
    
    if opcion == '1':
        ingrediente_extra = VEGETARIANOS[0]
    elif opcion == '2':
        ingrediente_extra = VEGETARIANOS[1]
    else:
        print("\nOpción de ingrediente no válida. Se añadirán solo los ingredientes base.")
        ingrediente_extra = None  # Usamos None para indicar que no se eligió un extra.

elif tipo_pizza == 'n':
    pizza_elegida = "No Vegetariana"
    
    # Mostrar opciones no vegetarianas
    print("\nIngredientes no vegetarianos disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    
    opcion = input("Elija un ingrediente extra (1, 2 o 3): ")
    
    if opcion == '1':
        ingrediente_extra = NO_VEGETARIANOS[0]
    elif opcion == '2':
        ingrediente_extra = NO_VEGETARIANOS[1]
    elif opcion == '3':
        ingrediente_extra = NO_VEGETARIANOS[2]
    else:
        print("\nOpción de ingrediente no válida. Se añadirán solo los ingredientes base.")
        ingrediente_extra = None

else:
    # Manejo de entrada no válida para el tipo de pizza
    print("\nError: Tipo de pizza no reconocido. El programa finaliza.")
    exit()

# Determinar la lista final de ingredientes
if ingrediente_extra:
    ingredientes_finales = f"{INGREDIENTES_BASE}, {ingrediente_extra}"
else:
    ingredientes_finales = INGREDIENTES_BASE

# Escribir el resultado en pantalla
print("\n" + "="*50)
print(f"RESUMEN DEL PEDIDO:")
print(f"Tipo de Pizza: {pizza_elegida}")
print(f"Ingredientes: {ingredientes_finales}")
print("="*50)