from utils.helpers import mostrar_titulo, mostrar_error, pausa


def menu_reportes(catalogo, prestamos):
    while True:
        mostrar_titulo("GESTION DE REPORTES")

        print("[1] Registrar usuario")
        print("[2] Eliminar usuario")
        print("[3] Historial de un usuario")
        print("[0] Volver")
        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "0":
            break
        else:
            mostrar_error("Opción inválida")
            pausa()

