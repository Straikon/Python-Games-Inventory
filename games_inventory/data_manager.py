# data_manager.py
#Se encarga de manejar el almacenamiento local: cargar, guardar y modificar el archivo JSON que guarda tu lista de juegos.

import json
import os

ARCHIVO_JUEGOS = "juegos.json"

def cargar_juegos():
    if not os.path.exists(ARCHIVO_JUEGOS):
        return []
    with open(ARCHIVO_JUEGOS, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_juegos(juegos):
    with open(ARCHIVO_JUEGOS, "w", encoding="utf-8") as f:
        json.dump(juegos, f, indent=4, ensure_ascii=False)

def agregar_juego(juego):
    juegos = cargar_juegos()
    juegos.append(juego)
    guardar_juegos(juegos)

