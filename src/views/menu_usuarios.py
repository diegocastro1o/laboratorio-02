from logica.usuarios import registrar_usuario, dar_baja_usuario, historial_usuario
from utils.helpers import mostrar_titulo, mostrar_error, pausa
from utils.models import Usuarios, Prestamos
from views.components import mostrar_historial_usuario


def menu_usuarios(usuarios: Usuarios, prestamos: Prestamos):
    while True:
        mostrar_titulo("GESTION DE USUARIOS")

        print("[1] Registrar usuario")
        print("[2] Eliminar usuario")
        print("[3] Historial de un usuario")
        print("[0] Volver")
        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n_socio = input('Ingrese el numero de socio del nuevo usuario a registrar: ')
            nombre = input('Ingrese el nombre del nuevo usuario a registrar: ')
            registrar_usuario(usuarios, n_socio, nombre)
            pausa()
        elif opcion == "2":
            n_socio = input('Ingrese el numero de socio del usuario a eliminar: ')
            dar_baja_usuario(usuarios, n_socio)
            pausa()
        elif opcion == "3":
            n_socio = input('Ingrese el numero de socio del historial a inspeccionar: ')
            historial = historial_usuario(prestamos, n_socio)
            if historial:
                mostrar_historial_usuario(historial, n_socio)
            pausa()
        elif opcion == "0":
            break
        else:
            mostrar_error("Opción inválida")
            pausa()
