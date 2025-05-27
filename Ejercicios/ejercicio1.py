#Ejercicio 1
frutas = {
    "Manzana": 20,
    "Mandarina": 15,
    "Mango": 25,
    "Plátano": 18,
    "Fresa": 30,
    "Frambuesa": 50
}

#Funcion para buscar una fruta, exacta o parcial
def buscarFruta(frutas):
    fruta = input("¿Ingresa el nombre de la fruta a buscar: ")
    for nombre, clave in frutas.items():
        if fruta.lower() in nombre.lower():
            print(f"{nombre} - ${clave}")

#Funcion para buscar un precio igual o menor de una fruta con el monto ingresado
def buscarPrecio(frutas):
    precio = int(input("Ingrese un precio de fruta: "))
    for nombre, clave in frutas.items():
        if clave <= precio:
            print(f"{nombre} - ${clave}")

#Funcion similar a buscar pero con variantes usando startswith
def buscar_por_inicio(frutas):
    fruta = input("¿Ingresa el incio de la fruta a buscar: ")
    for nombre, clave in frutas.items():
        if nombre.lower().startswith(fruta.lower()):
            print(f"{nombre} - ${clave}")

#Funcion similar a startswith pero con las ultimas letras
def buscar_por_fin(frutas):
    fruta = input("¿Ingresa el final de la fruta a buscar: ")
    encontrado = False  # ← bandera para saber si encontramos algo
    for nombre, clave in frutas.items():
        if nombre.lower().endswith(fruta.lower()):
            print(f"{nombre} - ${clave}")
            encontrado = True  # ← si encuentra, cambiamos la bandera
    if not encontrado:
        print(f"No se encontraron frutas que terminen con '{fruta}'.")

if __name__ == "__main__":
    buscar_por_fin(frutas)