from utils.constants import DATA_FILE
import json

# TODO: Parte de Diego

def guardar_datos(catalogo, usuarios, prestamos, ruta):
    data = dict(catalogo=catalogo, usuarios=usuarios, prestamos=prestamos)
    print(data)

def cargar_datos(ruta):
    with open(ruta, 'r') as file:
        data = json.load(file)
        return data.get("catalogo"), data.get("usuarios"), data.get("prestamos")

catalogo, usuarios, prestamos = cargar_datos(DATA_FILE)