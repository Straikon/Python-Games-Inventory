# 1. Lista de figuras
figuras = ["Goku", "Naruto", "Saitama"]
figuras2 = list(figuras)

# 2. Añadir una nueva figura
figuras.append("Luffy")
print("Lista despues de agregar Luffy:", figuras)
print(" ")
#Practica 1 lista antes y despues de agregar figura
print("Lista antes de antes de agregar una figura: ", figuras2)
print("Lista despues de agregar una figura: ", figuras)
print(" ")
# 3. Acceder a un elemento
print("Figura en la posicion 1:", figuras[1])  # Debería imprimir "Naruto"
print(" ")
# 4. Modificar un elemento
figuras[0] = "Vegeta"
print("Lista despues de cambiar 'Goku' por 'Vegeta':", figuras)
print(" ")
# 5. Diccionario con detalles de las figuras
inventario = {
    "Vegeta": {"anio": 2020, "disponible": True},
    "Naruto": {"anio": 2019, "disponible": False},
    "Saitama": {"anio": 2021, "disponible": True},
    "Luffy": {"anio": 2023, "disponible": True},
}

# 6. Acceder a la información del diccionario
print("Informacion de Vegeta:", inventario["Vegeta"])
print("Esta Naruto disponible?", inventario["Naruto"]["disponible"])

for figura, atributos in inventario.items():
    print(" ")
    print(f"{figura} - Anio:{atributos['anio']}, Disponibilidad:{atributos['disponible']}")