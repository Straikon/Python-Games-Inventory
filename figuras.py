# Funcion Menu
def menu():
    print("\n🎌 Inventario de Figuras de Anime 🎌")
    print("1️⃣- Agregar figura")
    print("2️⃣- Mostrar todas las figuras")
    print("3️⃣- Buscar figura")
    print("4️⃣- Salir 🚪")

# Funcion agregar
def agregar_figura(figuras):
    name = input("🧾 Nombre: ")
    year = int(input("📅 Año: "))
    cantidad = int(input("📦 Cantidad: "))
    figuras[name] = {"anio": year, "cantidad": cantidad}
    print(f"✅ ¡'{name}' agregada con éxito!")

# Funcion mostrar
def mostrar_figuras(figuras):
    print("\n📋 Lista de figuras:")
    for nombre, datos in figuras.items():
        print(f"✨ {nombre} - Año: {datos['anio']} - Cantidad: {datos['cantidad']}")

# Funcion Buscar
def buscar_figura(figuras):
    name = input("🔍 Nombre de la figura: ")
    if name in figuras[name].lower():
        datos = figuras[name]
        print(f"🧩 {name} - Año: {datos['anio']} - Cantidad: {datos['cantidad']}")
    else:
        print("❌ Figura no encontrada.")

#def modificar_figura():
    
# Funcion main, que ejecuta todo el programa
def main():
    figuras = {
        "Vegeta": {"anio": 2020, "cantidad": 10},
        "Naruto": {"anio": 2019, "cantidad": 5},
    }

    while True:
        menu()
        
        opcion = input("🔸 Opción: ")

        if opcion == "1":
            agregar_figura(figuras)
        elif opcion == "2":
            mostrar_figuras(figuras)
        elif opcion == "3":
            buscar_figura(figuras)
        elif opcion == "4":
            print("👋 ¡Hasta pronto, Iván!")
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()

"""
# Menu mas estatico
while True:
    print("1.- Agregar figura")
    print("2.- Mostrar todas las figuras")
    print("3.- Buscar Figura")
    print("4.- Salir")

    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
        name = input("Nombre de la figura: ")
        year = int(input("Año de salida: "))
        stock = int(input("Cantidad disponible: "))
        figuras[name] = {"anio": int(year), "cantidad": int(stock)}
        print("Figura agregada correctamente.")
    elif opcion == 2:
        print("\n Inventario de Figuras:")
        for figura, atributos in figuras.items():
            print(f"{figura} - Año: {atributos['anio']}, Cantidad: {atributos['cantidad']}")
    elif opcion == 3:
            buscar = input("Nombre de la figura a buscar: ")
            if buscar in figuras:
                datos = figuras[buscar]
                print(f"{buscar} - Año: {datos['anio']}, Cantidad: {datos['cantidad']}")
            else:
                print("Figura no encontrada.")
    elif opcion == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
        
# Menu mas estructurado
while True:
    print("\n🎌 Inventario de Figuras de Anime 🎌")
    print("1️⃣- Agregar figura")
    print("2️⃣- Mostrar todas las figuras")
    print("3️⃣- Buscar figura")
    print("4️⃣- Salir 🚪")

    opcion = input("🔸 Ingresa una opción: ")

    if opcion == "1":
        name = input("🧾 Nombre de la figura: ")
        year = input("📅 Año: ")
        cantidad = input("📦 Cantidad disponible: ")
        figuras[name] = {
            "anio": int(year),
            "cantidad": int(cantidad)
        }
        print(f"✅ ¡Figura '{name}' agregada con éxito!")

    elif opcion == "2":
        print("\n📋 Lista de figuras:")
        for figura, atributos in figuras.items():
            print(f"✨ {figura} - Año: {atributos['anio']} - Cantidad: {atributos['cantidad']}")

    elif opcion == "3":
        buscar = input("🔍 Ingresa el nombre de la figura a buscar: ")
        if buscar in figuras:
            datos = figuras[buscar]
            print(f"🧩 {buscar} - Año: {datos['anio']} - Cantidad: {datos['cantidad']}")
        else:
            print("❌ Figura no encontrada.")

    elif opcion == "4":
        print("👋 ¡Hasta luego, Iván! Sigue practicando 💻")
        break

    else:
        print("⚠️ Opción inválida. Intenta nuevamente.")
"""