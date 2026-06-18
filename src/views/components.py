from utils.helpers import mostrar_titulo, pausa
from utils.models import Catalogo


def despedida():
    mostrar_titulo("HASTA LUEGO", "Gracias por usar la Biblioteca UCU")
    exit()


def mostrar_catalogo(catalogo: Catalogo):
    mostrar_titulo("CATALOGO")

    print(f"{'ISBN':<10} {'Titulo':<25} {'Autor':<20} {'Disp.':>5}")
    print("-" * 65)

    for isbn in catalogo:
        libro = catalogo[isbn]
        print(
            f"{libro['ISBN']:<10} "
            f"{libro['titulo'][:24]:<25} "
            f"{libro['autor'][:19]:<20} "
            f"{libro['ejemplares_disponibles']:>5}"
        )

    pausa()
