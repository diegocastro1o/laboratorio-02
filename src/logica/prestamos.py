from persistencia import catalogo, usuarios, prestamos
from datetime import date
from utils.models import Usuarios, Catalogo, Prestamos
from persistencia import cargar_datos
from utils.constants import DATA_FILE


def registrar_prestamo(catalogo: Catalogo, usuarios: Usuarios, prestamos: Prestamos,
                        numero_socio: str, isbn: str, fecha_prestamo: str):
    try:
        if isbn not in catalogo or numero_socio not in usuarios:
            raise KeyError("El usuario no existe o el libro no está en el catálogo")
 
        if catalogo[isbn]["ejemplares_disponibles"] == 0:
            raise ValueError("No hay ejemplares disponibles")
 
        fecha_limite = (date.fromisoformat(fecha_prestamo) + timedelta(days=7)).isoformat()
 
        nuevo_prestamo = {
            "numero_socio": numero_socio,
            "ISBN": isbn,
            "fecha_prestamo": fecha_prestamo,
            "fecha_limite": fecha_limite,
            "devuelto": False
        }
 
        prestamos.append(nuevo_prestamo)
        catalogo[isbn]["ejemplares_disponibles"] -= 1
        usuarios[numero_socio]["prestamos_activos"].append(isbn)
 
        guardar_datos(catalogo=catalogo, usuarios=usuarios, prestamos=prestamos)
 
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
 
 
def registrar_devolucion(usuarios: Usuarios, catalogo: Catalogo, prestamos: Prestamos,
                          numero_socio: str, isbn: str):
    try:
        encontrado = False
        for prestamo in prestamos:
            if prestamo["numero_socio"] == numero_socio and prestamo["ISBN"] == isbn:
                prestamo["devuelto"] = True
                catalogo[isbn]["ejemplares_disponibles"] += 1
                if isbn in usuarios[numero_socio]["prestamos_activos"]:
                    usuarios[numero_socio]["prestamos_activos"].remove(isbn)
                encontrado = True
                break
 
        if not encontrado:
            raise ValueError("No se encontró un préstamo activo para ese usuario y libro")
 
        guardar_datos(catalogo=catalogo, usuarios=usuarios, prestamos=prestamos)
 
    except KeyError as e:
        print(f"Error: falta la clave {e} en los datos")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
 
 
def listar_vencidos(prestamos: Prestamos, fecha_actual: date):
    lista_vencidos = []
    try:
        for prestamo in prestamos:
            if fecha_actual.isoformat() > prestamo["fecha_limite"]:
                lista_vencidos.append(prestamo)
        print(lista_vencidos)
    except KeyError as e:
        print(f"Error: falta la clave {e} en algún préstamo")
    except Exception as e:
        print(f"Error inesperado al listar vencidos: {e}")
    return lista_vencidos
 
 
try:
    data = cargar_datos(DATA_FILE)
    prestamos, usuarios, catalogo = data['prestamos'], data['usuarios'], data['catalogo']
 
    registrar_prestamo(catalogo, usuarios, prestamos, "001", "978-2", "2026-08-09")
 
except Exception as e:
    print(f"Error al cargar los datos iniciales: {e}")
    
    
    
    
    
    
    

print(catalogo)
print(usuarios)
print(prestamos)
