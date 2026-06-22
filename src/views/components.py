from utils.helpers import mostrar_titulo, pausa, Colores
from utils.models import Catalogo, Prestamos, Resultado
from datetime import date


def despedida():
    mostrar_titulo("HASTA LUEGO", "Gracias por usar la Biblioteca UCU")
    exit()


def mostrar_catalogo(libros: Resultado, titulo: str = "CATÁLOGO"):
    mostrar_titulo(titulo)

    print(f"{'ISBN':<10} {'Titulo':<25} {'Autor':<20} {'Género':>6}")
    print("-" * 65)

    for libro in libros:
        print(
            f"{libro['ISBN']:<10} "
            f"{libro['titulo'][:24]:<25} "
            f"{libro['autor'][:19]:<20} "
            f"{libro['genero']:>6}"
        )


def mostrar_prestamos(prestamos: Prestamos, titulo: str = "PRÉSTAMOS"):
    mostrar_titulo(titulo)

    print(f"{'Socio':<10} {'ISBN':<10} {'Préstamo':<12} {'Limite':<12} {'Estado':<10}")
    print("-" * 60)
    
    for prestamo in prestamos:
        estado = "Devuelto" if prestamo["devuelto"] else "Activo"
        
        if date.today().isoformat() > prestamo["fecha_limite"]:
            estado = f"{Colores.ROJO}Vencido{Colores.RESET}"

        print(
            f"{prestamo['numero_socio']:<10} "
            f"{prestamo['ISBN']:<10} "
            f"{prestamo['fecha_prestamo']:<12} "
            f"{prestamo['fecha_limite']:<12} "
            f"{estado:<10}"
        )


def mostrar_historial_usuario(historial: Prestamos, numero_socio: str):
    mostrar_titulo(f"HISTORIAL DEL USUARIO {numero_socio}")

    print(f"{'ISBN':<10} {'Entrega':<12} {'Devolución':<12} {'Estado':<10}")
    print("-" * 50)

    for prestamo in historial:
        estado = f"{Colores.VERDE}Devuelto{Colores.RESET}" if prestamo["devuelto"] else "Activo"

        if date.today().isoformat() > prestamo["fecha_limite"] and estado == 'Activo':
            estado = f"{Colores.ROJO}Vencido{Colores.RESET}"

        print(
            f"{prestamo['ISBN']:<10} "
            f"{prestamo['fecha_prestamo']:<12} "
            f"{prestamo['fecha_limite']:<12} "
            f"{estado:<10}"
        )

