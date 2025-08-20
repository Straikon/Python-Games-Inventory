#Archivo donde se hara el uso de la API para buscar juegos
# Aquí está el código que se conecta a la API de RAWG para buscar juegos y obtener sus datos.

# api_client.py

import requests
import json
from config import API_KEY, URL_BASE

# Metodo que recibe una cadena y realizara una busqueda conectandose a la API
def buscar_juego(nombre):
#Estructura que arma el url con el que nos conectaremos a la API
    url = f"{URL_BASE}/games"
    params = {
        "key": API_KEY,
        "search": nombre,
        "page_size": 1
    }
    r = requests.get(url, params=params) # Variable a la que se le asginara la url
    if r.status_code == 200: # Condicional que hace una prueba para ver si la consulta fue correcta
        datos = r.json() # Dentro de datos vamos a guardar el archivo Json que retorno la API
        # Dentro del siguiente if vamos a obtener el resultado del juego que buscamos
        if datos["results"]: # Si datos obtuvo respuesta de la a API con la informacion deseada accedemos dentro del metodo
            juego = datos["results"][0] # Juego tomara el primer valor del diccionario con los resultados
            # Crearemos un nuevo diccionario en el que vamos almacenar 
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
        return {"error": f"Error en la API ({r.status_code})"}

def buscar_juego2(nombre):
    url = f"{URL_BASE}/games"
    params = {
        "key": API_KEY,
        "search": nombre,
        "page": 1,
        "page_size": 5
    }
    r = requests.get(url, params=params)
    
    if r.status_code == 200:
        data = r.json()
        resultados = []
        for juego in data.get("results", []):
            info = {
                "nombre": juego.get("name", "Desconocido"),
                "fecha": juego.get("released", "Desconocido"),
                "plataformas": [p["platform"]["name"] for p in juego.get("platforms", [])],
                "generos": [g["name"] for g in juego.get("genres", [])]
            }
            resultados.append(info)
        if resultados:
            return resultados
        else:
            return {"error": "No se encontró el juego"}
    else:
        return {"error": f"Error en la API ({r.status_code})"}