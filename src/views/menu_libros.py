from utils.helpers import mostrar_titulo, mostrar_error, pausa
from utils.models import Catalogo, Prestamos
from logica.libros import agregar_libro, eliminar_libro, buscar_libros




def menu_libros(catalogo: Catalogo, prestamos: Prestamos):
    while True:
        mostrar_titulo("GESTION DE LIBROS")

        print("[1] Agregar libro")
        print("[2] Eliminar libro")
        print("[3] Buscar libros")
        print("[4] Ver catalogo")
        print("[0] Volver")
        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            isbn = input('Ingrese ISBN del libro a agregar: ')
            title = input('Ingrese titulo del libro a agregar: ')
            aut = input('Ingrese autor del libro a agregar: ')
            genre = input('Ingrese género del libro a agregar: ')
            qty = input('Ingrese cantidad de ejemplares del libro a agregar: ')
            agregar_libro(catalogo, isbn, title, aut, genre, qty)
        elif opcion == "2":
            isbn = input('Ingrese ISBN del libro a agregar: ')
            eliminar_libro(catalogo, prestamos, isbn)
        elif opcion == "3":
            termino = input('Introduzca término de búsqueda: ')
            buscar_libros(catalogo, termino)
        elif opcion == "4":
            mostrar_catalogo(catalogo)
        elif opcion == "0":
            break
        else:
            mostrar_error("Opción inválida")
            pausa()

