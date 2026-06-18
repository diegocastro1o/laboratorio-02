from utils.helpers import mostrar_titulo, mostrar_error, pausa
from utils.models import Catalogo, Usuarios, Prestamos
from views.components import despedida
from views.menu_libros import menu_libros
from views.menu_prestamos import menu_prestamos
from views.menu_usuarios import menu_usuarios
from views.menu_reportes import menu_reportes


def contar_prestamos_activos(prestamos):
    cantidad = 0

    for prestamo in prestamos:
        if not prestamo["devuelto"]:
            cantidad += 1

    return cantidad


def menu_principal(catalogo: Catalogo, usuarios: Usuarios, prestamos: Prestamos):
    while True:
        mostrar_titulo("BIBLIOTECA UCU 2026", "Sistema de Gestion Bibliotecaria")

        print(f"Catalogo: {len(catalogo)} libros")
        print(f"Usuarios: {len(usuarios)} socios")
        print(f"Prestamos activos: {contar_prestamos_activos(prestamos)}")
        print()
        print("[1] Gestion de libros")
        print("[2] Gestion de usuarios")
        print("[3] Gestion de prestamos")
        print("[4] Reportes")
        print("[0] Salir")
        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_libros(catalogo, prestamos)
        elif opcion == "2":
            menu_usuarios(usuarios, prestamos)
        elif opcion == "3":
            menu_prestamos(catalogo, usuarios, prestamos)
        elif opcion == "4":
            # menu_reportes(prestamos)
            pass
        elif opcion == "0":
            despedida()
        else:
            mostrar_error("Opción inválida")
            pausa()