from logica.persistencia import guardar_datos
from utils.helpers import mostrar_exito, mostrar_error
from utils.models import Usuarios,Prestamos

def registrar_usuario(usuarios: Usuarios, numero_socio: str, nombre: str):
    try:
        if numero_socio in usuarios:
            raise Exception(f"Ya existe un usuario con el Nº {numero_socio}")

        usuarios[numero_socio] = {
            "numero_socio": numero_socio,
            "nombre": nombre,
            "prestamos_activos": []
        }

        guardar_datos(usuarios=usuarios)
        mostrar_exito(f'El usuario Nº {numero_socio}, {nombre} ha sido registrado')

    except Exception as e:
         mostrar_error(str(e))


def dar_baja_usuario(usuarios:Usuarios, numero_socio:str):
    try:
        if numero_socio not in usuarios:
            raise Exception("El Nº de socio ingresado no pertenece a ningún usuario existente")

        if usuarios[numero_socio]["prestamos_activos"]:
            raise Exception("El usuario posee prestamos activos o vencidos")

        usuarios.pop(numero_socio)
        guardar_datos(usuarios=usuarios)
        mostrar_exito('El usuario fue eliminado correctamente')

    except Exception as e:
        mostrar_error(str(e))



def historial_usuario(prestamos:Prestamos, numero_socio:str):
    try:
        historial: Prestamos = []

        for prestamo in prestamos:
            if prestamo["numero_socio"] == numero_socio:
                historial.append(prestamo)

        if not historial:
            raise Exception("El usuario no ha solicitado ningún préstamo.")

        return historial

    except Exception as e:
        mostrar_error(str(e))
