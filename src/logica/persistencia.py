from utils.constants import DATA_FILE
from utils.helpers import mostrar_exito
from utils.models import Catalogo, Usuarios, Prestamos, DataBiblioteca
from pathlib import Path
import json


def cargar_datos(ruta: Path = DATA_FILE) -> DataBiblioteca:
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return {
                'catalogo': data.get('catalogo', {}),
                'usuarios': data.get('usuarios', {}),
                'prestamos': data.get('prestamos', []),
            }

    except FileNotFoundError:
        raise Exception('No se encontró el archivo de datos.')

    except json.JSONDecodeError:
        raise Exception('El archivo de datos no tiene un JSON válido.')

    except PermissionError:
        raise Exception('No hay permisos para leer el archivo de datos.')

    except OSError:
        raise Exception('Ocurrió un error al cargar los datos.')


def guardar_datos(
    catalogo: Catalogo | None = None,
    usuarios: Usuarios | None = None,
    prestamos: Prestamos | None = None,
    ruta: Path = DATA_FILE
):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if catalogo is not None:
            data['catalogo'] = catalogo
        if usuarios is not None:
            data['usuarios'] = usuarios
        if prestamos is not None:
            data['prestamos'] = prestamos

        with open(ruta, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        mostrar_exito('Los cambios han sido persistidos exitosamente')

    except FileNotFoundError:
        raise Exception('No se encontró el archivo de datos.')

    except json.JSONDecodeError:
        raise Exception('El archivo de datos no tiene un JSON válido.')

    except PermissionError:
        raise Exception('No hay permisos para escribir el archivo de datos.')

    except OSError:
        raise Exception('Ocurrió un error al guardar los datos.')
