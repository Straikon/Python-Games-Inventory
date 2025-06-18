# ====================== #
#   Funciones del menu   #
# ====================== #

def menu():
    print("\nINVENTARIO DE VIDEOJUEGOS")
    print("1.- Agregar nuevo videojuego")
    print("2.- Ver todos los videojuegos")
    print("3.- Buscar informacion de un videojuego")
    print("4.- Actualizar registro de un videojuego")
    print("5.- Eliminar un videojuego")
    print("0.- Salir")
    
    opcion = int(input("Ingresar opcion: "))
    
    menu_options(opcion)

def menu_options(opc):
    list_games = []
    while True:
        if opc == 1:
            add_game(list_games)
        elif opc == 2:
            view_games(list_games)
        elif opc == 3:
            search_game()
            pass
        elif opc == 4:
            update_game()
            pass
        elif opc == 5:
            delete_game()
            pass
        elif opc == 0:
            print("Saliendo del programa")
        else:
            print("Opcion invalida, ingrese una opcion del menu anterior")

# =========================== #
#   Funciones de estructura   #
# =========================== #

def add_game(lista_juegos):
    nombre = input("🎮 Nombre del juego: ").strip()
    # Año de lanzamiento (lo pedimos como texto para validarlo después)
    anio_input = input("📅 Año de lanzamiento: ").strip()
    # Captura de plataformas
    plataformas = []
    primera_vez = len(lista_juegos) == 0
    while True:
        plataforma = input("🕹️ Ingresa una plataforma: ").strip()
        if plataforma:
            plataformas.append(plataforma)
        otra = input("¿Deseas agregar otra plataforma? (s/n): ").lower()
        if otra != "s":
            break
    # Estado del juego (opcional)
    terminado_input = input("✅ ¿Ya lo terminaste? (s/n, opcional): ").lower()
    terminado = terminado_input == "s"
    # Validación separada
    errores = validar_juego(nombre, plataformas, anio_input, primera_vez)
    if errores:
        print("\n❌ No se pudo agregar el juego por los siguientes errores:")
        for error in errores:
            print(error)
        return
    # Conversión segura del año
    anio = int(anio_input)
    # Diccionario del juego
    juego = {
        "nombre": nombre,
        "plataformas": plataformas,
        "anio": anio,
        "estatus": terminado
    }
    lista_juegos.append(juego)
    print(f"\n🎉 ¡'{nombre}' agregado correctamente!\n")

def view_games(lista_juegos):
    for juego in lista_juegos:
        print(f"Nombre: {juego['nombre']}, Pltaforma(s): {juego['plataformas']}, Fecha de salida: {juego['anio']}, Estatus: {juego['estatus']} ")

def search_game():
    pass

def update_game():
    pass

def delete_game():
    pass

# ======================================= #
#   Funciones de validacion/ Auxiliares   #
# ======================================= #

def validar_juego(nombre, plataformas, anio, primera_vez):
    errores = []
    if not nombre.strip():
        errores.append("❌ El nombre del juego es obligatorio.")
    if primera_vez and not plataformas:
        errores.append("❌ Debes ingresar al menos una plataforma la primera vez.")
    if not str(anio).isdigit():
        errores.append("❌ El año de salida debe ser un número.")
    return errores

if __name__ == "__main__":
    menu()