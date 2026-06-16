from persistencia import catalogo, usuarios, prestamos
from datetime import datetime, timedelta

# TODO: Agregar los models (tipado de entidades) en los parámetros de la función.
#       Importar de `utils.models` solo los necesarios (ej: `from utils.models import Usuarios,...`)
#       y aplicarlos a cada parametro (ej: `usuarios: Usuarios`)

# TODO: El diccionario `nuevoPrestamo` definirlo por extensión. Ejm:
#       nuevoPrestamo = {
#       "isbn": isbn
#       ...
#       }

def registrar_prestamo (catalogo, usuarios, prestamos, numero_socio, isbn, fecha_prestamo):
    if isbn not in catalogo or numero_socio not in usuarios :
        print('Error: el usuario no existe o no hay ejemplares del libro')
    
    elif catalogo[isbn]["ejemplares_disponibles"] == 0:
        print("Error: no hay ejemplares disponibles")
        
    else:
        nuevoPrestamo = {
        fecha_limite == (datetime.strptime(fecha_prestamo, "%d/%m/%Y") + timedelta(days=7)).strftime("%d/%m/%Y")
        "numero_socio" = numero_socio
        "isbn" = isbn
        "fecha_prestamo" = fecha_prestamo
        "fecha_limite" = fecha_limite
        "devuelto" = False
        }
        prestamos.append(nuevoPrestamo)
        
        catalogo[isbn]["ejemplares_disponibles"] -= 1
        usuarios[numero_socio]["prestamos_activos"].append(isbn)
        
        



print(catalogo)
print(usuarios)
print(prestamos)
