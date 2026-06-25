from utils.helpers import mostrar_titulo, pausa, Colores
from utils.models import Catalogo, Prestamos, Resultado
from datetime import date


def despedida():
    mostrar_titulo('HASTA LUEGO', 'Gracias por usar la Biblioteca UCU')
    exit()


def mostrar_catalogo(libros: Resultado, titulo: str = 'CATÁLOGO'):
    mostrar_titulo(titulo)

    print('{:<10} {:<25} {:<20} {:>6}'.format('ISBN', 'Titulo', 'Autor', 'Género'))
    print('-' * 65)

    for libro in libros:
        print('{:<10} {:<25} {:<20} {:>6}'.format(
            libro['ISBN'],
            libro['titulo'][:24],
            libro['autor'][:19],
            libro['genero']
        ))


def mostrar_prestamos(prestamos: Prestamos, titulo: str = 'PRÉSTAMOS'):
    mostrar_titulo(titulo)

    print('{:<10} {:<10} {:<12} {:<12} {:<10}'.format('Socio', 'ISBN', 'Préstamo', 'Limite', 'Estado'))
    print('-' * 60)
    
    for prestamo in prestamos:
        estado = f'{Colores.VERDE}Devuelto{Colores.RESET}' if prestamo['devuelto'] else 'Activo'
        
        if date.today().isoformat() > prestamo['fecha_limite'] and not prestamo['devuelto']:
            estado = f'{Colores.ROJO}Vencido{Colores.RESET}'

        print('{:<10} {:<10} {:<12} {:<12} {:<10}'.format(
            prestamo['numero_socio'],
            prestamo['ISBN'],
            prestamo['fecha_prestamo'],
            prestamo['fecha_limite'],
            estado
        ))


def mostrar_historial_usuario(historial: Prestamos, numero_socio: str):
    mostrar_titulo(f'HISTORIAL DEL USUARIO {numero_socio}')

    print('{:<10} {:<12} {:<12} {:<10}'.format('ISBN', 'Entrega', 'Devolución', 'Estado'))
    print('-' * 50)

    for prestamo in historial:
        estado = f'{Colores.VERDE}Devuelto{Colores.RESET}' if prestamo['devuelto'] else 'Activo'

        if date.today().isoformat() > prestamo['fecha_limite'] and not prestamo['devuelto']:
            estado = f'{Colores.ROJO}Vencido{Colores.RESET}'

        print('{:<10} {:<12} {:<12} {:<10}'.format(
            prestamo['ISBN'],
            prestamo['fecha_prestamo'],
            prestamo['fecha_limite'],
            estado
        ))
