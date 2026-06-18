import os

# Cambia las vocales con tilde por vocales sin tilde
def normalizar(palabra):
    vocales_esp = ['á', 'é', 'í', 'ó', 'ú']
    vocales = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(vocales_esp)):
        if vocales_esp[i] in palabra:
            palabra = palabra.replace(vocales_esp[i], vocales[i])

    return palabra


class Colores:
    RESET = "\033[0m"
    ROJO = "\033[91m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    CYAN = "\033[96m"
    NEGRITA = "\033[1m"


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    elif os.environ.get("TERM"):
        os.system("clear")


def linea(ancho=60):
    print("=" * ancho)


def mostrar_titulo(titulo, subtitulo=""):
    limpiar_pantalla()
    print(Colores.CYAN + Colores.NEGRITA)

    linea()
    print(titulo.center(60))

    if subtitulo:
        print(subtitulo.center(60))

    linea()
    print(Colores.RESET)


def mostrar_error(mensaje):
    print(f"{Colores.ROJO}[ERROR]{Colores.RESET} {mensaje}")


def mostrar_exito(mensaje):
    print(f"{Colores.VERDE}[OK]{Colores.RESET} {mensaje}")


def pausa():
    input("\nPresione Enter para continuar...")



