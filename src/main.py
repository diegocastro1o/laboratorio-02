from logica.persistencia import cargar_datos, guardar_datos
from utils.constants import DATA_FILE
from views.menu_principal import menu_principal

data = cargar_datos(DATA_FILE)
prestamos, usuarios, catalogo = data['prestamos'], data['usuarios'], data['catalogo']


menu_principal(catalogo, usuarios, prestamos)




