from logica.persistencia import cargar_datos, guardar_datos
from utils.constants import DATA_FILE
from datetime import date, timedelta

data = cargar_datos(DATA_FILE)
prestamos, usuarios, catalogo = data['prestamos'], data['usuarios'], data['catalogo']

# Todo: Acá va el código del menú interactivo del usuario

prestamos.append({
    'numero_socio': '001',
    'ISBN': '978-1',
    'fecha_prestamo': date.today().isoformat(),
    'fecha_limite': (date.today() + timedelta(days=14)).isoformat(),
    'devuelto': False,
})

print(guardar_datos(catalogo, usuarios, prestamos, DATA_FILE))


