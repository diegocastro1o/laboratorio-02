from logica.persistencia import cargar_datos
from utils.constants import DATA_FILE
from views.menu_principal import menu_principal

def main():
    data = cargar_datos(DATA_FILE)
    prestamos, usuarios, catalogo = data['prestamos'], data['usuarios'], data['catalogo']

    menu_principal(catalogo, usuarios, prestamos)

if __name__ == '__main__':
    main()
