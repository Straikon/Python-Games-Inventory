# main.py
# Es el punto de entrada del programa. 
# Aquí se junta todo: se pide el nombre del juego, se busca con api_client, se guarda con data_manager y se muestra la lista.

from api_client import buscar_juego2
from data_manager import agregar_juego, cargar_juegos

def main():
    nombre = input("Escribe el nombre del juego a buscar: ")
    resultado = buscar_juego2(nombre)
    if "error" in resultado:
        print("Error:", resultado["error"])
    else:
        agregar_juego(resultado)
        print("Juego agregado:")
        print(resultado)
        print("\nLista completa de juegos:")
        juegos = cargar_juegos()
        for j in juegos:
            print(f"- {j['nombre']} ({j['fecha']})")

def mostrar():
    nombre = input("Escribe el nombre del juego a buscar: ")
    resultado = buscar_juego2(nombre)
    for search in resultado:
        print(f"Nombre: {search['nombre']}\nFecha lanzamiento: {search['fecha']}\nPlataformas: {search['plataformas']}\nGeneros: {search['generos']}")
        print("--------------------------------------------------")

if __name__ == "__main__":
    mostrar()
