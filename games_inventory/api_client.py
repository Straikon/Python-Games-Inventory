#Archivo donde se hara el uso de la API para buscar juegos
# Aquí está el código que se conecta a la API de RAWG para buscar juegos y obtener sus datos.

# api_client.py

import requests
import json
from config import API_KEY, URL_BASE

def buscar_juego(nombre):
    url = URL_BASE + '/game/'
    params = {
        "key": API_KEY,
        "search": nombre,
        "page_size": 1
    }

    respuesta = requests.get(url, params=params)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos["results"]:
            juego = datos["results"][0]
            resultado = {
                "nombre": juego.get("name", "Desconocido"),
                "fecha": juego.get("released", "Desconocido"),
                "plataformas": [p["platform"]["name"] for p in juego.get("platforms", [])],
                "generos": [g["name"] for g in juego.get("genres", [])]
            }
            return resultado
        else:
            return {"error": "No se encontró el juego"}
    else:
        return {"error": "Error en la API"}

