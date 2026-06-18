from utils.models import Catalogo, Prestamos
def agregar_libro (catalogo:Catalogo, isbn:str, titulo:str, autor:str, genero:str, ejemplares:int):
    for id in catalogo:
        if id == isbn:
            return 'El libro ya esta registrado'
    nuevo_libro = {
        'ISBN': isbn,
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'ejemplares_totales': ejemplares,
        'ejemplares_disponibles': ejemplares
    }
    catalogo[isbn]=nuevo_libro
    return catalogo



def eliminar_libro (catalogo:Catalogo, prestamos:Prestamos, isbn:str):
    if isbn not in catalogo:
        return 'El libro no existe. NO ES POSIBLE ELIMINAR'
    for pr in prestamos:
        if pr['ISBN']==isbn:
            return 'El libro tiene un prestamo pendiente. NO ES POSIBLE ELIMINAR'
    return catalogo.pop(isbn)

def buscar_libros(catalogo:Catalogo, termino:str):
    lista_busqueda=[]
    for lib in catalogo.values:
        if lib in lista_busqueda:
            continue
        if termino == lib['titulo']:
            lista_busqueda.append(lib)
            continue
        if termino == lib['genero']:
            lista_busqueda.append(lib)
            continue
        if termino == lib['autor']:
            lista_busqueda.append(lib)
    return lista_busqueda



