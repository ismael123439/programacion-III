from contextlib import contextmanager

@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    # Abrir el archivo utilizando los parámetros recibidos
    archivo = open(ruta_archivo, modo)
    try:
        # Usar yield para devolver el objeto archivo
        yield archivo
    finally:
        # Asegurarse de que el archivo se cierre correctamente
        archivo.close()

def leer_archivo(ruta_archivo):
    try:
        # Usar el context manager para abrir el archivo en modo lectura
        with gestionar_archivo(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        # Manejar adecuadamente la excepción de archivo no encontrado
        print(f"Error: El archivo '{ruta_archivo}' no se encuentra.")
    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        print(f"Ocurrió un error: {e}")

def escribir_archivo(ruta_archivo, lineas):
    # Usar el context manager para abrir el archivo en modo escritura
    with gestionar_archivo(ruta_archivo, 'w') as archivo:
        for linea in lineas:
            archivo.write(linea + '\n')

# Ejemplo de uso
lineas_para_escribir = [
    "Esta es la primera línea.",
    "Esta es la segunda línea.",
    "Esta es la tercera línea."
]

escribir_archivo('archivo_ejemplo.txt', lineas_para_escribir)
leer_archivo('archivo_ejemplo.txt')
