from persistencia import catalogo, usuarios, prestamos
from datetime import datetime
from utils.models import Usuarios, Catalogo, Prestamos
from persistencia import cargar_datos
from utils.constants import DATA_FILE


def registrar_prestamo (catalogo: Catalogo, usuarios: Usuarios, prestamos: Prestamos , numero_socio: str, isbn: str, fecha_prestamo: str):
    if isbn not in catalogo or numero_socio not in usuarios :
        print('Error: el usuario no existe o no hay ejemplares del libro')
    
    elif catalogo[isbn]["ejemplares_disponibles"] == 0:
        print("Error: no hay ejemplares disponibles")
    else:
        fecha_limite = (datetime.strptime(fecha_prestamo, "%d/%m/%Y") + timedelta(days=7)).strftime("%d/%m/%Y")
        nuevoPrestamo = {
            "numero_socio" : numero_socio
            "ISBN" : isbn
            "fecha_prestamo" : fecha_prestamo
            "fecha_limite" : fecha_limite
            "devuelto" : False
        }
        prestamos.append(nuevoPrestamo)
        catalogo[isbn]["ejemplares_disponibles"] -= 1
        usuarios[numero_socio]["prestamos_activos"].append(isbn)

def registrar_devolucion(usuarios: Usuarios ,catalogo: Catalogo , prestamos: Prestamos, numero_socio: str, isbn: str):
    for prestamo in prestamos:
        if prestamo["numero_socio"] == numero_socio and prestamo["isbn"] == isbn:
            prestamo["devuelto"] = True
            catalogo[isbn]["ejemplares_disponibles"] += 1

def listar_vencidos(prestamos: Prestamos, fecha_actual):
    lista_vencidos = []
    for prestamo in prestamos:
        fecha_actual = datetime.today()
        if fecha_actual > prestamo["fecha_limite"]:
            lista_vencidos.append(prestamo)
    return lista_vencidos
            
    
    
data = cargar_datos(DATA_FILE)
prestamos, usuarios, catalogo = data['prestamos'], data['usuarios'], data['catalogo']   
    
registrar_prestamo(usuarios, catalogo, prestamos, "001" , "978-2", "09/08/2026"  )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        



print(catalogo)
print(usuarios)
print(prestamos)
