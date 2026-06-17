from persistencia import cargar_datos
from utils.models import Usuarios,Prestamos
from utils.constants import DATA_FILE


#ln (registro usuario):1) existe usuario ?
#                             si: lanzas excepcion
#                             no: crear diccionario del nuevo usuario
#                      2)agregarlo a al diccionario "usuario"
def registrar_usuario(usuarios:Usuarios, numero_socio:str, nombre:str):
    try:
        if numero_socio in usuarios:
            raise Exception ("Usuario existente", usuarios[numero_socio])
        usuarios[numero_socio]={
                            "numero_socio": numero_socio,
                            "nombre": nombre,
                            "prestamos_activos": []
                            }       
        return usuarios
    except Exception as e:
        print(e)
    

#LN (dar de baja usuario) existe usuario ?
        #                 no: lanzar excepcion
        #                 si: tiene prestamos activos?
        #                       si: lanzar excepcion
        #                       no: borrar usuario del diccionario usuario
class PrestamosException(Exception):
    pass

def dar_baja_usuario(usuarios:Usuarios, prestamos:Prestamos,numero_socio:str):
    try:     
        if numero_socio in usuarios:
            if usuarios[numero_socio]["prestamos_activos"]==[]:
                del usuarios[numero_socio]
            else:
                raise PrestamosException("El usuario tiene prestamos activo,no se puede dar de baja",ususario[numero_socio][prestamos_activos])
        else:
            raise KeyError("El usuario no existe")
        
        
    except PrestamosException as e:
        print(e)
    except KeyError as b:
        print(b)
    

#LN (historial prestamos) buscar en la lista de prestamos , si hay algo con numero_socio elegido
                        # crear lista vacia y si los prestamos son del numero_socio, agregarlo a la lista vacia
                        # la lista devolveria el numero_socio con el isbn y si fue devuelto o no
                        #exceptions si : no existe socio
def historial_usuario(prestamos:Prestamos, numero_socio:str):
    try:
        lista=[]
        n=len(prestamos)
        verificador=0
        for x in range(n):
            if prestamos[x]["numero_socio"]==numero_socio:
                lista.append(prestamos[x]) 
        if len(lista)==0:
            raise KeyError("El usuario no existe")
        return lista
    
    except KeyError as e:
        print(e)

data = cargar_datos(DATA_FILE)
prestamos, usuarios, catalogo = data['prestamos'], data['usuarios'], data['catalogo']
print(registrar_usuario(usuarios,'002', 'PPSP'))