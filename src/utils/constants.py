from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE_DIR / "data.json"

# Cambia las vocales con tilde por vocales sin tilde
def normalizar(palabra):
    vocales_esp = ['á', 'é', 'í', 'ó', 'ú']
    vocales = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(vocales_esp)):
        if vocales_esp[i] in palabra:
            palabra = palabra.replace(vocales_esp[i], vocales[i])

    return palabra
