from utils.models import Catalogo, Usuarios, Prestamos, DataBiblioteca
import json

# TODO: Parte de Diego


def cargar_datos(ruta) -> DataBiblioteca:
    with open(ruta, 'r') as file:
        data = json.load(file)
        return {
            "catalogo": data.get("catalogo", {}),
            "usuarios": data.get("usuarios", {}),
            "prestamos": data.get("prestamos", []),
        }


def guardar_datos(catalogo: Catalogo, usuarios: Usuarios, prestamos: Prestamos, ruta):
    data = dict(catalogo=catalogo, usuarios=usuarios, prestamos=prestamos)

    with open(ruta, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    return cargar_datos(ruta)