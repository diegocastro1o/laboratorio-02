from utils.helpers import mostrar_titulo, mostrar_error, pausa
from utils.models import Catalogo, Prestamos, Usuarios
from logica.libros import agregar_libro, eliminar_libro, buscar_libros, recomendar_libros
from views.components import mostrar_catalogo


def menu_libros(catalogo: Catalogo, prestamos: Prestamos, usuarios: Usuarios):
    while True:
        mostrar_titulo('GESTIÓN DE LIBROS')

        print('[1] Agregar libro')
        print('[2] Eliminar libro')
        print('[3] Buscar libros')
        print('[4] Ver catalogo')
        print('[5] Recomendación personalizada')
        print('[0] Volver')
        print()

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            isbn = input('Ingrese ISBN del libro a agregar: ')
            title = input('Ingrese titulo del libro a agregar: ')
            aut = input('Ingrese autor del libro a agregar: ')
            genre = input('Ingrese género del libro a agregar: ')
            qty = int(input('Ingrese cantidad de ejemplares del libro a agregar: '))
            agregar_libro(catalogo, isbn, title, aut, genre, qty)
            pausa()

        elif opcion == '2':
            isbn = input('Ingrese ISBN del libro a eliminar: ')
            eliminar_libro(catalogo, prestamos, isbn)
            pausa()

        elif opcion == '3':
            termino = (input('Introduzca término de búsqueda: ')).lower()
            libros = buscar_libros(catalogo, termino)

            if libros:
                mostrar_catalogo(libros, 'Resultados búsqueda')

            pausa()

        elif opcion == '4':
            mostrar_catalogo(catalogo.values())
            pausa()

        elif opcion == '5':
            n_socio = input('Ingrese su número de socio: ')
            n = int(input('Ingrese la cantidad máxima de recomendaciones deseada: '))
            recomendaciones = recomendar_libros(catalogo, prestamos, usuarios, n_socio, n)

            if recomendaciones:
                mostrar_catalogo(recomendaciones, f'Recomendaciones para el socio Nº{n_socio}')

            pausa()

        elif opcion == '0':
            break

        else:
            mostrar_error('Opción inválida')
            pausa()
