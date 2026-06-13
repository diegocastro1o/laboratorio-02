from persistencia import catalogo, usuarios, prestamos
from datetime import datetime, timedelta
# TODO: Parte de Male

def registrar_prestamo (catalogo, usuarios, prestamos, numero_socio, isbn, fecha_prestamo):
    if isbn not in catalogo or numero_socio not in usuarios :
        print('Error: el usuario no existe o no hay ejemplares del libro')
    
    elif catalogo[isbn]["ejemplares_disponibles"] == 0:
        print("Error: no hay ejemplares disponibles")
        
    else:
        nuevoPrestamo = {}
        fecha_limite = (datetime.strptime(fecha_prestamo, "%d/%m/%Y") + timedelta(days=7)).strftime("%d/%m/%Y")
        nuevoPrestamo["numero_socio"] = numero_socio
        nuevoPrestamo["isbn"] = isbn
        nuevoPrestamo["fecha_prestamo"] = fecha_prestamo
        nuevoPrestamo["fecha_limite"] = fecha_limite
        nuevoPrestamo["devuelto"] = False
        prestamos.append(nuevoPrestamo)
        
        catalogo[isbn]["ejemplares_disponibles"] -= 1
        usuarios[numero_socio]["prestamos_activos"].append(isbn)
        
        



print(catalogo)
print(usuarios)
print(prestamos)
