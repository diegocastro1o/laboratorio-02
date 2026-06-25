from datetime import date, timedelta
from logica.persistencia import guardar_datos
from utils.helpers import mostrar_error, mostrar_exito
from utils.models import Usuarios, Catalogo, Prestamos, Prestamo


def registrar_prestamo(catalogo: Catalogo, usuarios: Usuarios, prestamos: Prestamos, numero_socio: str, isbn: str,
                       fecha_prestamo: str):
    try:
        if isbn not in catalogo:
            raise Exception('El libro no forma parte de nuestra colección')

        if numero_socio not in usuarios:
            raise Exception('El usuario ingresado no existe')

        if catalogo[isbn]['ejemplares_disponibles'] == 0:
            raise Exception('No hay ejemplares disponibles')

        fecha_limite = (date.fromisoformat(fecha_prestamo) + timedelta(days=7)).isoformat()
        nuevo_prestamo: Prestamo = {
            'numero_socio': numero_socio,
            'ISBN': isbn,
            'fecha_prestamo': fecha_prestamo,
            'fecha_limite': fecha_limite,
            'devuelto': False
        }
        prestamos.append(nuevo_prestamo)
        catalogo[isbn]['ejemplares_disponibles'] -= 1
        usuarios[numero_socio]['prestamos_activos'].append(isbn)

        guardar_datos(catalogo, usuarios, prestamos)
        mostrar_exito('El préstamo se ha registrado exitosamente')

    except Exception as e:
        mostrar_error(str(e))


def registrar_devolucion(usuarios: Usuarios, catalogo: Catalogo, prestamos: Prestamos, numero_socio: str, isbn: str):
    try:
        if numero_socio not in usuarios:
            raise Exception('El usuario ingresado no existe')

        if isbn not in catalogo:
            raise Exception('El libro no forma parte de nuestra colección')


        devuelto = False

        for prestamo in prestamos:
            cond = prestamo['numero_socio'] == numero_socio and prestamo['ISBN'] == isbn and isbn in usuarios[numero_socio][
                'prestamos_activos'] and not prestamo['devuelto']

            if cond:
                prestamo['devuelto'] = True
                catalogo[isbn]['ejemplares_disponibles'] += 1
                usuarios[numero_socio]['prestamos_activos'].remove(isbn)

                devuelto = True

                guardar_datos(catalogo, usuarios, prestamos)
                break

        if not devuelto:
            raise Exception('El usuario nunca solicitó ese libro')

    except Exception as e:
        mostrar_error(str(e))


def listar_vencidos(prestamos: Prestamos, fecha_actual: str):
    try:
        lista_vencidos: Prestamos = []
        for prestamo in prestamos:
            if fecha_actual > prestamo['fecha_limite'] and not prestamo['devuelto']:
                lista_vencidos.append(prestamo)

        if not lista_vencidos:
            raise Exception('No hay préstamos vencidos')

        return lista_vencidos

    except Exception as e:
        mostrar_error(str(e))
