#ln (registro usuario):1) existe usuario ?
#                             si: lanzas excepcion
#                             no: crear diccionario del nuevo usuario
#                      2)agregarlo a al diccionario "usuario"
def registrar_usuario(usuarios, numero_socio, nombre):
    if numero_socio in usuarios:
        #excepcion 
    else:
        usuarios[numero_socio]={
                                  "numero_socio": numero_socio,
                                  "nombre": nombre,
                                  "prestamos_activos": []
                                }
        
#LN (dar de baja usuario) existe usuario ?
        #                 no: lanzar excepcion
        #                 si: tiene prestamos activos?
        #                       si: lanzar excepcion
        #                       no: borrar usuario del diccionario usuario
def dar_baja_usuario(usuarios, prestamos,numero_socio):
    if numero_socio in usuarios:
        if usuarios[numero_socio]["prestamos_activos"]==[]:
            del usuarios[numero_socio]
        else:
            #excepcion
    else:
        #excepcion
        
#LN (historial prestamos) buscar en la lista de prestamos , si hay algo con numero_socio elegido
                        # crear lista vacia y si los prestamos son del numero_socio, agregarlo a la lista vacia
                        # la lista devolveria el numero_socio con el isbn y si fue devuelto o no
def historial_usuario(prestamos, numero_socio):
    lista=[]
    n=len(prestamos)
    for x in range(n):
        if prestamos[x]["numero_socio"]==numero_socio:
            lista.append(prestamos[x])
    return lista
        