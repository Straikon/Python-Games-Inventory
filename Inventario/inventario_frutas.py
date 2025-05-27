import archivo_csv

def menu():
    lista_frutas = archivo_csv.cargar_desde_archivo()
    
    while True:
        print("1.-Agregar")
        print("2.-Mostrar")
        print("3.-Actualizar")
        print("4.-Eliminar")
        print("5.-Buscar")
        print("0.-Salir")
        
        opc = int(input("Ingrese una opcion del menu: "))
        
        if opc == 1:
            agregar_fruta(lista_frutas)
        elif opc == 2:
            mostrar_fruta(lista_frutas) 
            pass
        elif opc == 3:
            actualizar_fruta(lista_frutas)
        elif opc == 4:
            eliminar_fruta(lista_frutas)
        elif opc == 5:
            buscar_fruta(lista_frutas)
        elif opc == 0:
            print("Saliendo del programa... Gracias por usarlo")
            break
        else:
            print("Opcion incorrecta")

def agregar_fruta(lista_frutas):
    while True:
        n_fruta = input("Nombre de la fruta: ")
        # Verificamos si ya existe usando el método 'repetido'
        encontrado = encontrar_fruta(lista_frutas, n_fruta)
        if encontrado != -1:
            print(f"La fruta '{n_fruta}' ya existe.")
        else:# Si no existe, la agregamos
            p_fruta = int(input("Precio $: "))
            e_fruta = int(input("Existencia: "))
            lista_frutas.append({
            "nombre": n_fruta,
            "precio": p_fruta,
            "existencia": e_fruta})
            print("Fruta agregada")
            archivo_csv.guardar_en_archivo(lista_frutas)
            return

def encontrar_fruta(lista_frutas, fruta):
    for i, fruta_index in enumerate(lista_frutas):
        if fruta_index["nombre"].lower() == fruta.lower():
            return i
    return -1

def mostrar_fruta(lista_frutas):
    for fruta in lista_frutas:
        print(f"Nombre: {fruta['nombre']}, Precio: ${fruta['precio']}, Existencia: {fruta['existencia']} ")

def actualizar_fruta(lista_frutas):
    mostrar_fruta(lista_frutas)
    upd_fruta = input("Ingrese el nombre de la fruta a actualizar: ")
    encontrado = encontrar_fruta(lista_frutas, upd_fruta)
    if encontrado != -1:
        lista_frutas[encontrado]["precio"] = int(input("Nuevo precio $: "))
        lista_frutas[encontrado]["existencia"] = int(input("Nueva existencia: "))
        print("Fruta actualizada correctamente.")
    else:
        print(f"La fruta '{upd_fruta}' no fue encontrada.")

def eliminar_fruta(lista_frutas):
    mostrar_fruta(lista_frutas)
    del_fruta = input("Ingrese el nombre de la fruta a eliminar: ")
    encontrado = encontrar_fruta(lista_frutas, del_fruta)
    if encontrado != -1:
        lista_frutas.pop(encontrado)
        print("Fruta eliminada correctamente.")
    else:
        print(f"La fruta '{del_fruta}' no fue encontrada.")

def buscar_fruta(lista_frutas):
    bus_fruta = input("Ingresa una fruta a buscar: ")
    for fruta in lista_frutas:
        for key, value in fruta.items():
            if bus_fruta.lower() in fruta["nombre"].lower():
                print(key, value)

if __name__ == "__main__":
    menu()