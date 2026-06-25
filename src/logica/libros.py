from logica.usuarios import historial_usuario
from utils.helpers import mostrar_error, mostrar_exito, normalizar
from utils.models import Catalogo, Prestamos, Libro, Resultado, Usuarios
from logica.persistencia import guardar_datos
from random import randint

def agregar_libro (catalogo:Catalogo, isbn:str, titulo:str, autor:str, genero:str, ejemplares:int):
    try:
        for id_libro in catalogo:
            if id_libro == isbn:
                raise Exception('El libro ya esta registrado')

        nuevo_libro: Libro = {
            'ISBN': isbn,
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'ejemplares_totales': ejemplares,
            'ejemplares_disponibles': ejemplares
        }

        catalogo[isbn]=nuevo_libro
        guardar_datos(catalogo=catalogo)

        mostrar_exito('El libro ha sido agregado correctamente')

    except Exception as e:
        mostrar_error(str(e))


def eliminar_libro (catalogo:Catalogo, prestamos:Prestamos, isbn:str):
    try:
        if isbn not in catalogo:
            raise Exception('El libro no existe. NO ES POSIBLE ELIMINAR')

        for prestamo in prestamos:
            if prestamo['ISBN'] == isbn and not prestamo['devuelto']:
                raise Exception('El libro tiene un préstamo pendiente. NO ES POSIBLE ELIMINAR')

        catalogo.pop(isbn)
        guardar_datos(catalogo=catalogo, prestamos=prestamos)

        mostrar_exito('El libro ha sido eliminado correctamente')

    except Exception as e:
        mostrar_error(str(e))


def buscar_libros(catalogo:Catalogo, termino:str):
    try:
        lista_busqueda=[]
        for libro in catalogo.values():
            if libro in lista_busqueda:
                continue

            comparaciones = [normalizar(libro['titulo'].lower()), normalizar(libro['genero'].lower()), normalizar(libro['autor'].lower())]

            for comparacion in comparaciones:
                if normalizar(termino) in comparacion:
                    lista_busqueda.append(libro)
                    continue

        if not lista_busqueda:
            raise Exception('Ningún libro coincide con lo solicitado')

        return lista_busqueda

    except Exception as e:
        mostrar_error(str(e))


def recomendar_libros(catalogo: Catalogo, prestamos: Prestamos, usuarios:Usuarios , numero_socio: str, n: int):
    try:
        historial = historial_usuario(prestamos, numero_socio, usuarios)

        if not historial:
            raise Exception(f'No tenemos información suficiente del usuario Nº{numero_socio}')

        generos_leidos = dict()
        libros_leidos = list()
        for prestamo in historial:
            isbn = prestamo['ISBN']
            genero = catalogo[isbn]['genero']

            generos_leidos[genero] = generos_leidos.get(genero, 0) + 1
            libros_leidos.append(isbn)

        generos_ordenados = []
        for genero, qty in generos_leidos.items():
            if not generos_ordenados:
                generos_ordenados.append((genero, qty))
                continue

            insertado = False

            for i in range(len(generos_ordenados)):
                if qty > generos_ordenados[i][1]:
                    generos_ordenados.insert(i, (genero, qty))
                    insertado = True
                    break

            if not insertado:
                generos_ordenados.append((genero, qty))

        resultado = []
        recomendaciones: Resultado = []

        for libro in catalogo.values():
            generos = []
            for i in range(3):
                if len(generos_ordenados) > i:
                    generos.append(generos_ordenados[i][0])

            if libro['genero'] in generos and libro['ISBN'] not in libros_leidos:
                resultado.append(libro)

        if len(resultado) < n:
            raise Exception(f'No hay {n} libros que se adapten a los gustos del usuario')

        while len(recomendaciones) < n:
            for libro in resultado:
                if not len(recomendaciones) < n:
                    break

                if randint(0, 1) and libro not in recomendaciones:
                    recomendaciones.append(libro)

        return recomendaciones

    except Exception as e:
        mostrar_error(str(e))
