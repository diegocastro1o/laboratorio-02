from logica.prestamos import registrar_prestamo, registrar_devolucion, listar_vencidos
from utils.helpers import mostrar_titulo, mostrar_error, pausa
from utils.models import Catalogo, Usuarios, Prestamos
from views.components import mostrar_prestamos
from datetime import date

def menu_prestamos(catalogo: Catalogo, usuarios: Usuarios, prestamos: Prestamos):
    while True:
        mostrar_titulo('GESTION DE PRÉSTAMOS')

        print('[1] Registrar préstamo')
        print('[2] Registrar devolución')
        print('[3] Listar préstamos vencidos')
        print('[0] Volver')
        print()

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            n_socio = input('Ingrese el numero de socio que solicita el préstamo: ')
            isbn = input('Ingrese el ISBN del libro solicitado: ')
            fecha_actual = date.today().isoformat()
            registrar_prestamo(catalogo, usuarios, prestamos, n_socio, isbn, fecha_actual)
            pausa()
        elif opcion == '2':
            n_socio = input('Ingrese el numero de socio que devuelve el libro: ')
            isbn = input('Ingrese el ISBN del libro a devolver: ')
            registrar_devolucion(usuarios, catalogo, prestamos, n_socio, isbn)
            pausa()
        elif opcion == '3':
            fecha_actual = date.today().isoformat()
            vencidos = listar_vencidos(prestamos, fecha_actual)
            
            if vencidos:
                mostrar_prestamos(vencidos, 'PRÉSTAMOS VENCIDOS')

            pausa()
        elif opcion == '0':
            break
        else:
            mostrar_error('Opción inválida')
            pausa()
