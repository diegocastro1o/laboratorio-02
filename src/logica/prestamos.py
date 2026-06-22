from datetime import date, timedelta
from logica.persistencia import guardar_datos
from utils.helpers import mostrar_error, mostrar_exito
from utils.models import Usuarios, Catalogo, Prestamos, Prestamo


def registrar_prestamo(catalogo: Catalogo, usuarios: Usuarios, prestamos: Prestamos, numero_socio: str, isbn: str,
                       fecha_prestamo: str):
    if isbn not in catalogo or numero_socio not in usuarios:
        print('Error: el usuario no existe o no hay ejemplares del libro')
    elif catalogo[isbn]["ejemplares_disponibles"] == 0:
        print("Error: no hay ejemplares disponibles")
    else:
        fecha_limite = (date.fromisoformat(fecha_prestamo) + timedelta(days=7)).isoformat()
        nuevo_prestamo: Prestamo = {
            "numero_socio": numero_socio,
            "ISBN": isbn,
            "fecha_prestamo": fecha_prestamo,
            "fecha_limite": fecha_limite,
            "devuelto": False
        }
        prestamos.append(nuevo_prestamo)
        catalogo[isbn]["ejemplares_disponibles"] -= 1
        usuarios[numero_socio]["prestamos_activos"].append(isbn)

        guardar_datos(catalogo, usuarios, prestamos)
        mostrar_exito("El préstamo se ha registrado exitosamente")


def registrar_devolucion(usuarios: Usuarios, catalogo: Catalogo, prestamos: Prestamos, numero_socio: str, isbn: str):
    for prestamo in prestamos:
        if prestamo["numero_socio"] == numero_socio and prestamo["ISBN"] == isbn:
            prestamo["devuelto"] = True
            catalogo[isbn]["ejemplares_disponibles"] += 1
            usuarios[numero_socio]["prestamos_activos"].remove(isbn)

            guardar_datos(catalogo, usuarios, prestamos)


def listar_vencidos(prestamos: Prestamos, fecha_actual: str):
    try:
        lista_vencidos: Prestamos = []
        for prestamo in prestamos:
            if fecha_actual > prestamo["fecha_limite"] and not prestamo["devuelto"]:
                lista_vencidos.append(prestamo)

        if not lista_vencidos:
            raise Exception('No hay préstamos vencidos')

        return lista_vencidos

    except Exception as e:
        mostrar_error(str(e))

