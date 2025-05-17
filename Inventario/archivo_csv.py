# archivo_csv.py
def guardar_en_archivo(lista_frutas, archivo="frutas.csv"):
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("nombre,precio,existencia\n")
        for fruta in lista_frutas:
            linea = f"{fruta['nombre']},{fruta['precio']},{fruta['existencia']}\n"
            f.write(linea)

def cargar_desde_archivo(archivo="frutas.csv"):
    lista = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            next(f)  # Saltamos el encabezado
            for linea in f:
                nombre, precio, existencia = linea.strip().split(",")
                lista.append({
                    "nombre": nombre,
                    "precio": int(precio),
                    "existencia": int(existencia)
                })
    except FileNotFoundError:
        print("📂 No se encontró el archivo. Se iniciará una lista vacía.")
    return lista
