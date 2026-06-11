from persistencia import usuarios, prestamos

# TODO: Parte de Juanma
print(usuarios)
print(prestamos)


def registrar_usuario(usuarios, numero_socio, nombre):
    if numero_socio in usuarios:
        print("Error")
            # excepcion
    else:
        usuarios[numero_socio]={
                                  "numero_socio": numero_socio,
                                  "nombre": nombre,
                                  "prestamos_activos": []
                                }

def dar_baja_usuario(usuarios, prestamos,numero_socio):
    if numero_socio in usuarios:
        if usuarios[numero_socio]["prestamos_activos"] == []:
            del usuarios[numero_socio]
        # else:
            # excepcion
    # else:
        # excepcion

def historial_usuario(prestamos, numero_socio):
    lista=[]
    n=len(prestamos)
    for x in range(n):
        if prestamos[x]["numero_socio"]==numero_socio:
            lista.append(prestamos[x])
    return lista