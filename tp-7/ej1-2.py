from contextlib import contextmanager

@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    archivo = open(ruta_archivo, modo)
    try:
        yield archivo
    finally:
        archivo.close()
