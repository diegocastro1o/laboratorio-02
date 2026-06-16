from typing import TypedDict, TypeAlias


class Libro(TypedDict):
    ISBN: str
    titulo: str
    autor: str
    genero: str
    ejemplares_totales: int
    ejemplares_disponibles: int


class Usuario(TypedDict):
    numero_socio: str
    nombre: str
    prestamos_activos: list[str]


class Prestamo(TypedDict):
    numero_socio: str
    ISBN: str
    fecha_prestamo: str
    fecha_limite: str
    devuelto: bool


Catalogo: TypeAlias = dict[str, Libro]
Usuarios: TypeAlias = dict[str, Usuario]
Prestamos: TypeAlias = list[Prestamo]


class DataBiblioteca(TypedDict):
    catalogo: Catalogo
    usuarios: Usuarios
    prestamos: Prestamos
